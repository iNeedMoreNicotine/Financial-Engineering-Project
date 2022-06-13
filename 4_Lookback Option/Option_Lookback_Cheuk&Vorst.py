from math import sqrt, exp

def lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type):
    dt = T/layers
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    mu = exp((r-q)*dt)
    pWave = (mu*u - 1)/(mu * (u-d))

    uNodes = []
    for i in range(layers+1):
        uNodes.append([0]*(i+1))

    for i in range(layers+1):
        for j in range(i+1):
            if j == i:
                uNodes[i][j] = 1
            else:
                uNodes[i][j] = u**(i-j)

    # backward induction
    putValues = []
    for j in range(layers+1):
        putValues.append(max(uNodes[layers][j] - 1, 0))
    
    times = 0
    i_temp = layers-1
    while times < layers:
        for j in range(i_temp+1):
            if j == i_temp:
                putValues[j] = ((1-pWave) * putValues[j] + pWave * putValues[j+1]) * mu * exp(-r*dt)
            else:
                putValues[j] = ((1-pWave) * putValues[j] + pWave * putValues[j+2]) * mu * exp(-r*dt)
        putValues.pop()

        if type == 'American':
            for j in range(i_temp+1):
                putValues[j] = max(putValues[j], uNodes[i_temp][j] - 1)

        times += 1
        i_temp -= 1
    
    print(f'(CRR Binomial Tree) Price of {type} Lookback Put : {round(putValues[0]*St, 4)} (Cheuk & Vorst)')
    return putValues[0]*St




# main
St = 50
T = 0.25
r = 0.1
q = 0
sigma = 0.4


layers = 100
print('======================================================================')
type = 'European'
print(f'{type} Lookback Option')
print(f'[ Smax,t = {St} ]')
print('----------------------------------------------------------------------')
print(f'n = {layers}')
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
print()

print('======================================================================')
type = 'American'
print(f'{type} Lookback Option')
print(f'[ Smax,t = {St} ]')
print('----------------------------------------------------------------------')
print(f'n = {layers}')
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
print()

layers = 300
print('======================================================================')
type = 'European'
print(f'{type} Lookback Option')
print(f'[ Smax,t = {St} ]')
print('----------------------------------------------------------------------')
print(f'n = {layers}')
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
print()

print('======================================================================')
type = 'American'
print(f'{type} Lookback Option')
print(f'[ Smax,t = {St} ]')
print('----------------------------------------------------------------------')
print(f'n = {layers}')
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
print()

layers = 1000
print('======================================================================')
type = 'European'
print(f'{type} Lookback Option')
print(f'[ Smax,t = {St} ]')
print('----------------------------------------------------------------------')
print(f'n = {layers}')
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
print()

print('======================================================================')
type = 'American'
print(f'{type} Lookback Option')
print(f'[ Smax,t = {St} ]')
print('----------------------------------------------------------------------')
print(f'n = {layers}')
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
print()