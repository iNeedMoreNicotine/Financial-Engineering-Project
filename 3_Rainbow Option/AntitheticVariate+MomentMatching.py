from math import log, exp, sqrt
import numpy as np


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
                cov_matrix[i][j] = round(sigma_lst[i]**2, 6)
            else:
                try:
                    cov_matrix[i][j] = round(sigma_lst[i] * sigma_lst[j] * rho_dict[f'rho{i+1}{j+1}'], 6)
                except:
                    cov_matrix[i][j] = round(sigma_lst[i] * sigma_lst[j] * rho_dict[f'rho{j+1}{i+1}'], 6)

    return cov_matrix

def rainbow_MC_AntitheticVariate(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, call_put):
    parameters = dict()
    for j in range(asset_amount):
        parameters[f'S{j+1}, sigma{j+1}, q{j+1}'] = (S0_lst[j], sigma_lst[j], q_lst[j])
    # print(parameters)

    # multiply sigma_lst with sqrt(T)
    sigma_lst_T = []
    for j in range(asset_amount):
        sigma_lst_T.append(sigma_lst[j]*sqrt(T))
    
    cov_matrix = construct_cov_matrix(asset_amount, sigma_lst_T, rho_dict)
    A = cholesky_decomposition(cov_matrix)
    A = np.array(A)
    # for row in cov_matrix:
    #     print(row)

    meanValuesLst = []
    times = 0
    while times < reps:
        stockSamples = []
        zzz = []
        # Antithetic Variate
        for _ in range(int(sims/2)):
            z = []
            z_negative = []
            for j in range(asset_amount):
                z.append(np.random.standard_normal())
            for j in range(asset_amount):
                z_negative.append(-z[j])
            zzz.append(z)
            zzz.append(z_negative)

        respectiveMeans = []
        respectiveSD = []
        for j in range(asset_amount):
            temp = []
            try:
                for i in range(sims):
                    temp.append(zzz[i][j])
            # 假如sims不為偶數
            except:
                print('-----------------------------------------------------')
                print('!! Exception : sims 輸入為奇數 --> sims = sims - 1 !!')
                print('-----------------------------------------------------')
                sims -= 1
                for i in range(sims):
                    temp.append(zzz[i][j])
            respectiveMeans.append(np.mean(temp))
            respectiveSD.append(np.std(temp))
        

        # Moment Matching
        for j in range(asset_amount):
            for i in range(sims):
                zzz[i][j] = (zzz[i][j] - respectiveMeans[j])/respectiveSD[j]

        pairedSample = []
        for i in range(sims):
            zzz[i] = np.array(zzz[i])
            pairedSample.append(zzz[i].dot(A))
        
        means = []
        for j in range(asset_amount):
            Sj = parameters[f'S{j+1}, sigma{j+1}, q{j+1}'][0]
            sigmaj = parameters[f'S{j+1}, sigma{j+1}, q{j+1}'][1]
            qj = parameters[f'S{j+1}, sigma{j+1}, q{j+1}'][2]
            meanj = log(Sj) + (r - qj - 0.5*(sigmaj**2)) * T
            means.append(meanj)
        for j in range(asset_amount):
            for i in range(sims):
                pairedSample[i][j] += means[j]
                pairedSample[i][j] = exp(pairedSample[i][j])
        for i in range(sims):
            stockSamples.append(pairedSample[i].tolist())

        optionValue = []
        if call_put == 'call on max':
            for pair in stockSamples:
                callValue = max(max(pair) - K, 0)
                optionValue.append(callValue)

        elif call_put == 'call on min':
            for pair in stockSamples:
                callValue = max(min(pair) - K, 0)
                optionValue.append(callValue)

        elif call_put == 'put on max':
            for pair in stockSamples:
                putValue = max(K - max(pair), 0)
                optionValue.append(putValue)

        else:
            for pair in stockSamples:
                putValue = max(K - min(pair), 0)
                optionValue.append(putValue)

        discounted = np.mean(optionValue) * exp(-r * T)
        meanValuesLst.append(discounted)
        times += 1

    temp_str = ''
    str_lst = call_put.split(' ')
    for word in str_lst:
        if word == 'on':
            temp_str = temp_str + word + ' '
        else:
            temp_str = temp_str + word.capitalize() + ' '
    temp_str = temp_str.strip()

    sdOfRep = np.std(meanValuesLst)
    meanOfRep = np.mean(meanValuesLst)
    upperBound = meanOfRep + 2*sdOfRep
    upperBound = round(upperBound, 4)
    lowerBound = meanOfRep - 2*sdOfRep
    lowerBound = round(lowerBound, 4)
    bounds = [lowerBound, upperBound]
    print("==================================================")
    print(f"Rainbow Option : European {temp_str}")
    print("==================================================")
    print(f"[ Asset amount = {asset_amount} ]")
    print("--------------------------------------------------")
    print(f"Mean : {round(meanOfRep, 4)}")
    print(f"Standard Error : {round(sdOfRep, 4)}")
    print(f"95% C.I. : {bounds}")
    print()

    return meanOfRep





# main
asset_amount = 5
S0_lst = [95, 95, 95, 95, 95]
K = 100
T = 0.5
r = 0.01
q_lst = [0.05, 0.04, 0.06, 0.03, 0.04]
sigma_lst = [0.5, 0.5, 0.5, 0.5, 0.5]
rho_dict = {'rho12': 0.5, 'rho13': 0.4, 'rho14': 0.3, 'rho15': 0.2, 'rho23':0.5, 'rho24':0.4, 'rho25':0.3, 'rho34':0.5, 'rho35':0.4, 'rho45':0.3}
sims = 30000
reps = 20

rainbow_MC_AntitheticVariate(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'call on max')
rainbow_MC_AntitheticVariate(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'call on min')
rainbow_MC_AntitheticVariate(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'put on max')
rainbow_MC_AntitheticVariate(asset_amount, S0_lst, K, T, r, q_lst, sigma_lst, rho_dict, sims, reps, 'put on min')