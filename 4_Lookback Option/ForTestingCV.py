from math import sqrt, exp

def lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type):
    dt = T/layers
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    mu = exp((r-q)*dt)
    pWave = (mu*u - 1)/(mu * (u-d))

    uNodes = []
    for i in range(layers):
        temp = []
        for j in range(i+2):
            temp.append(0)
        uNodes.append(temp)

    for i in range(layers):
        for j in range(i+2):
            if j == i+1:
                uNodes[i][j] = 1
            else:
                uNodes[i][j] = u**(i+1-j)
    
    # backward induction
    callValues = []
    for j in range(layers+1):
        callValues.append(max(1 - uNodes[layers-1][j]**-1, 0))
    
    times = 0
    counter = layers
    while times < layers:
        for j in range(counter):
            if j == counter - 1:
                callValues[j] = (pWave * callValues[j] + (1-pWave) * callValues[j+1]) * mu * exp(-r*dt)
                break
            else:
                callValues[j] = (pWave * callValues[j] + (1-pWave) * callValues[j+2]) * mu * exp(-r*dt)
        callValues.pop()
        # print(putValues)

        if type == 'American':
            for j in range(counter-1):
                callValues[j] = max(callValues[j], uNodes[counter-2][j]**-1)

        times += 1
        counter -= 1
    
    print(f'(CRR Binomial Tree) Price of {type} Lookback Put : {round(callValues[0]*St, 4)} (Cheuk & Vorst)')
    return callValues[0]*St

St = 100
T = 0.5
r = 0.04
q = 0.07
type = 'European'

print('--------------------------------------------------')
sigma = 0.1
layers = 50
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
layers = 100
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
layers = 500
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
layers = 1000
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)

print('--------------------------------------------------')
sigma = 0.2
layers = 50
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
layers = 100
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
layers = 500
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
layers = 1000
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)

print('--------------------------------------------------')
sigma = 0.3
layers = 50
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
layers = 100
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
layers = 500
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
layers = 1000
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)