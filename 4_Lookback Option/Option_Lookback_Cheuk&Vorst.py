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
    putValues = []
    for j in range(layers+1):
        putValues.append(max(uNodes[layers-1][j] - 1, 0))
    
    times = 0
    counter = layers
    while times < layers:
        for j in range(counter):
            if j == counter - 1:
                putValues[j] = ((1-pWave) * putValues[j] + pWave * putValues[j+1]) * mu * exp(-r*dt)
                break
            else:
                putValues[j] = ((1-pWave) * putValues[j] + pWave * putValues[j+2]) * mu * exp(-r*dt)
        putValues.pop()

        if type == 'American':
            for j in range(counter-1):
                putValues[j] = max(putValues[j], uNodes[counter-2][j] - 1)

        times += 1
        counter -= 1
    
    print(f'(CRR Binomial Tree) Price of {type} Lookback Put : {round(putValues[0]*St, 4)} (Cheuk & Vorst)')
    return putValues[0]*St




# main
St = 50
T = 0.25
r = 0.1
q = 0
sigma = 0.4

print('======================================================================')
type = 'European'
print(f'{type} Lookback Option')
print(f'[ Smax,t = {St} ]')
print('----------------------------------------------------------------------')
layers = 10000
print(f'n = {layers}')
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
print()

print('======================================================================')
type = 'American'
print(f'{type} Lookback Option')
print(f'[ Smax,t = {St} ]')
print('----------------------------------------------------------------------')
layers = 10000
print(f'n = {layers}')
lookback_CRR_CheukAndVorst(St, T, r, q, sigma, layers, type)
print()