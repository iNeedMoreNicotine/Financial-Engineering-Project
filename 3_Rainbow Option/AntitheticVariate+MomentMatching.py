from math import log, exp, sqrt
import numpy as np
from scipy.stats import norm
import scipy.linalg 

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




K = 100
r = 0.1
T = 0.5
# sims必須為偶數
sims = 10069
reps = 20
n = 5
S10, S20, S30, S40, S50 = 95, 95, 95, 95, 95
q1, q2, q3, q4, q5 = 0.05, 0.05, 0.05, 0.05, 0.05
sigma1, sigma2, sigma3, sigma4, sigma5 = 0.5, 0.5, 0.5, 0.5, 0.5




# main
sqDict = dict()
for i in range(n):
    sqDict[f'S{i+1}, sigma{i+1}, q{i+1}'] = (locals()[f'S{i+1}0'], locals()[f'sigma{i+1}'], locals()[f'q{i+1}'])
print(sqDict)
print('==============================================================================================================')
cov_matrix = [[sigma1**2*T, 0.5*sigma1*sigma2*T, 0.5*sigma1*sigma3*T, 0.5*sigma1*sigma4*T, 0.5*sigma1*sigma5*T],
              [0.5*sigma2*sigma1*T, sigma2**2*T, 0.5*sigma2*sigma3*T, 0.5*sigma2*sigma4*T, 0.5*sigma2*sigma5*T],
              [0.5*sigma3*sigma1*T, 0.5*sigma3*sigma2*T, sigma3**2*T, 0.5*sigma3*sigma4*T, 0.5*sigma3*sigma5*T],
              [0.5*sigma4*sigma1*T, 0.5*sigma4*sigma2*T, 0.5*sigma4*sigma3*T, sigma4**2*T, 0.5*sigma4*sigma5*T],
              [0.5*sigma5*sigma1*T, 0.5*sigma5*sigma2*T, 0.5*sigma5*sigma3*T, 0.5*sigma5*sigma4*T, sigma5**2*T]]
# cov_matrix = cov_matrix(n, sigmas, rhos)
print('Covariance Matrix: ')
print("--------------------")
for row in cov_matrix:
    print(row)
print('==============================================================================================================')

A = cholesky_decomposition(cov_matrix)
# A = scipy.linalg.cholesky(cov_matrix)
A = np.array(A)
meanValuesLst = []
times = 0
while times < reps:
    stockSamples = []
    zzz = []
    # Antithetic variate + moment matching
    for i in range(int(sims/2)):
        z = []
        z_negative = []
        for i in range(n):
            z.append(np.random.standard_normal())
        for i in range(n):
            z_negative.append(-z[i])
        zzz.append(z)
        zzz.append(z_negative)

    respectiveMeans = []
    respectiveSD = []
    for i in range(n):
        temp = []
        try:
            for j in range(sims):
                temp.append(zzz[j][i])
        # 假如sims不為偶數
        except:
            print('-----------------------------------------------------')
            print('!! Exception : sims 輸入為奇數 --> sims = sims - 1 !!')
            print('-----------------------------------------------------')
            sims -= 1
            for j in range(sims):
                temp.append(zzz[j][i])
        respectiveMeans.append(np.mean(temp))
        respectiveSD.append(np.std(temp))
    
    for i in range(n):
        for j in range(sims):
            zzz[j][i] = (zzz[j][i] - respectiveMeans[i])/respectiveSD[i]

    pairedSample = []
    for j in range(sims):
        zzz[j] = np.array(zzz[j])
        pairedSample.append(zzz[j].dot(A))
    
    means = []
    for i in range(n):
        SI = sqDict[f'S{i+1}, sigma{i+1}, q{i+1}'][0]
        sigmaI = sqDict[f'S{i+1}, sigma{i+1}, q{i+1}'][1]
        qI = sqDict[f'S{i+1}, sigma{i+1}, q{i+1}'][2]
        meanI = log(SI) + (r - qI - 0.5*(sigmaI**2)) * T
        means.append(meanI)
    for i in range(n):
        for j in range(sims):
            pairedSample[j][i] += means[i]
            pairedSample[j][i] = exp(pairedSample[j][i])
    for j in range(sims):
        stockSamples.append(pairedSample[j].tolist())

    optionValue = []
    for pair in stockSamples:
        callValue = max(max(pair) - K, 0)
        optionValue.append(callValue)

    discounted = np.mean(optionValue) * exp(-r * T)
    meanValuesLst.append(discounted)
    times += 1


# print(meanValuesLst)
sdOfRep = np.std(meanValuesLst)
meanOfRep = np.mean(meanValuesLst)
upperBound = meanOfRep + 2*sdOfRep
upperBound = round(upperBound, 6)
lowerBound = meanOfRep - 2*sdOfRep
lowerBound = round(lowerBound, 6)
bounds = [lowerBound, upperBound]
print(f"Rainbow Option")
print("--------------------")
print(f"平均 : {round(meanOfRep, 6)}")
print(f"標準誤 : {round(sdOfRep, 6)}")
print(f"九十五趴信賴區間 : {bounds}")