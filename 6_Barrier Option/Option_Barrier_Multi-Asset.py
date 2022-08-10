from math import log, exp, sqrt
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt


def cholesky_decomposition(cov_matrix):
    A = []
    n = len(cov_matrix)
    for i in range(n):
        A.append([0]*n)

    # step1
    A[0][0] = cov_matrix[0][0]**0.5
    for j in range(1,n):
        A[0][j] = cov_matrix[0][j]/A[0][0]

    # step2&3
    if n > 2:
        for i in range(1, n-1):
            temp = []
            for k in range(i):
                temp.append(A[k][i]**2)
            A[i][i] = (cov_matrix[i][i]-sum(temp))**0.5

            for j in range(i+1,n):
                temp = []
                for k in range(i):
                    temp.append(A[k][i]*A[k][j])
                A[i][j] = (cov_matrix[i][j]-sum(temp))/A[i][i]

    # step4
    temp = []
    for k in range(n-1):
        temp.append((A[k][n-1])**2)
    A[n-1][n-1] = (cov_matrix[n-1][n-1] - sum(temp))**0.5

    return A

def construct_cov_matrix(n, sigma_lst, rho_dict):
    cov_matrix = []
    for i in range(n):
        temp = []
        for j in range(n):
           temp.append(0)
        cov_matrix.append(temp)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                cov_matrix[i][j] = sigma_lst[i]**2
            else:
                try:
                    cov_matrix[i][j] = sigma_lst[i] * sigma_lst[j] * rho_dict[f'rho{i+1}{j+1}']
                except:
                    cov_matrix[i][j] = sigma_lst[i] * sigma_lst[j] * rho_dict[f'rho{j+1}{i+1}']

    return cov_matrix

def barrier_multiasset_MC(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, B, n, sims, reps, barrier_type, call_put):
    parameters = dict()
    for j in range(asset_amount):
        parameters[f'S{j+1}, sigma{j+1}, q{j+1}'] = (S0_lst[j], sigma_lst[j], q_lst[j])
    # print(parameters)

    dt = T/n
    # multiply sigma_lst with sqrt(dt)
    sigma_lst_dt = []
    for j in range(asset_amount):
        sigma_lst_dt.append(sigma_lst[j]*sqrt(dt))

    # cov_matrix = [[sigma1**2*dt, 0.2*sigma1*sigma2*dt],
    #               [0.2*sigma2*sigma1*dt, sigma2**2*dt]]
    cov_matrix = construct_cov_matrix(asset_amount, sigma_lst_dt, rho_dict)
    A = cholesky_decomposition(cov_matrix)
    A = np.array(A)

    means = []
    for _ in range(reps):
        optionValues = []
        # for each simulation
        for sim in range(sims):
            # for each asset, simulate a price path 
            stockSamples = pd.DataFrame()
            for i in range(n+1):
                if i == 0:
                    for j in range(asset_amount):
                        stockSamples.loc[i, f'sample_asset{j+1}'] = log(parameters[f'S{j+1}, sigma{j+1}, q{j+1}'][0])
                else:
                    z = []
                    for j in range(asset_amount):
                        z.append(np.random.standard_normal())
                    z = np.array(z)
                    pairedSample = z.dot(A)
                    for j in range(asset_amount):
                        stockSamples.loc[i, f'sample_asset{j+1}'] = pairedSample[j] + (r - parameters[f'S{j+1}, sigma{j+1}, q{j+1}'][2] - parameters[f'S{j+1}, sigma{j+1}, q{j+1}'][1]**2/2)*dt

            stockSamples = stockSamples.cumsum()
            stockSamples = np.exp(stockSamples)
            # print(stockSamples)

            # minumum rainbow option
            # first, find the least performing equity
            for j in range(asset_amount):
                if j == 0:
                    lpe_price = stockSamples.loc[n, f'sample_asset{j+1}']
                    lpe_index = j+1
                else:  
                    if stockSamples.loc[n, f'sample_asset{j+1}'] < lpe_price:
                        lpe_price = stockSamples.loc[n, f'sample_asset{j+1}']
                        lpe_index = j+1
            # print(lpe_index)
            # print(lpe_price)

            if call_put == 'call':
                payoff = max(lpe_price - K, 0) * exp(-r * T)
            else:
                payoff = max(K - lpe_price, 0) * exp(-r * T)

            # decide terminal payoff according to the barrier
            # knock-out
            if barrier_type == 'up-and-out':
                if max(stockSamples[f'sample_asset{lpe_index}']) >= B:
                    optionValue = 0
                else:
                    optionValue = payoff

            elif barrier_type == 'down-and-out':
                if min(stockSamples[f'sample_asset{lpe_index}']) <= B:
                    optionValue = 0
                else:
                    optionValue = payoff

            # knock-in
            elif barrier_type == 'up-and-in':
                if max(stockSamples[f'sample_asset{lpe_index}']) >= B:
                    optionValue = payoff
                else:
                    optionValue = 0
            else:
                if min(stockSamples[f'sample_asset{lpe_index}']) <= B:
                    optionValue = payoff
                else:
                    optionValue = 0
            optionValues.append(optionValue)

            # plot the paths for checking...
            # for j in range(asset_amount):
            #     plt.plot(stockSamples[f'sample_asset{j+1}'])
            # plt.xlabel('Time')
            # plt.ylabel('Simulated Stock Price')
            # plt.axhline(y = B, color = 'red', linestyle = 'dashed')
            # min_xlim, max_xlim = plt.xlim()
            # plt.text((min_xlim + max_xlim)*0.75, B*0.95, f'option value : {round(optionValue, 4)}')
            # plt.show()
        
        mean = np.mean(optionValues)
        means.append(mean)

    sdOfRep = np.std(means)
    meanOfRep = np.mean(means)
    upperBound = meanOfRep + 2*sdOfRep
    upperBound = round(upperBound, 4)
    lowerBound = meanOfRep - 2*sdOfRep
    lowerBound = round(lowerBound, 4)
    bounds = [lowerBound, upperBound]
    print('============================================================')
    print(f'Multi-Asset Barrier Option ({barrier_type}) : European {call_put}')
    print('============================================================')
    print(f'[ B = {B} ]')
    print('------------------------------------------------------------')
    print(f'Mean : {round(meanOfRep, 4)}')
    print(f'Standard Error : {round(sdOfRep, 4)}')
    print(f'95% C.I. : {bounds}')
    print()

    return meanOfRep




asset_amount = 2
S0_lst = [100, 100]
T = 0.5
r = 0.01
q_lst = [0.05, 0.06]
sigma_lst = [0.4, 0.4]
rho_dict = {'rho12': 0.5}
n = 125
sims = 50
reps = 20

barrier_multiasset_MC(asset_amount, S0_lst, 90, T, r, q_lst, sigma_lst, rho_dict, 110, n, sims, reps, 'up-and-out', 'call')
barrier_multiasset_MC(asset_amount, S0_lst, 80, T, r, q_lst, sigma_lst, rho_dict, 70, n, sims, reps, 'down-and-in', 'put')