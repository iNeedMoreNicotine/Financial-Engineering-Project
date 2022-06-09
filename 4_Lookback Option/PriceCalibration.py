from math import log, exp, sqrt

def calibratedPrice(stockPrice):
    last1 = stockPrice[-1]
    last2 = stockPrice[-2]
    calibration = sorted(last1 + last2, reverse = True)
    calibration[layers] = St
    caliIndex = []
    for i in range(layers,-layers-1,-1):
        caliIndex.append(i)
    calibration = dict(zip(caliIndex,calibration))

    for i in range(layers):
        for j in range(i+2):
            indexDiff = (i+1-j) - j
            stockPrice[i][j] = calibration[indexDiff]
            
    return stockPrice


StMax = 50
St = 50
T = 1/12
r = 0.1
q = 0
sigma = 0.4
layers = 6

dt = T/layers
u = exp(sigma * sqrt(dt))
d = exp(-sigma * sqrt(dt))
p = (exp((r-q)*dt) - d)/(u - d)

stockPrice = []
for i in range(2, layers+2):
    stockPrice.append([0]*i)
for i in range(layers):
    for j in range(i+2):
        stockPrice[i][j] = St * u**(i+1-j) * d**(j)
print('----------original-----------')
for i in stockPrice:
    print(i)
print('--------------------')

stockPrice = calibratedPrice(stockPrice)
print('----------calibrated-----------')
for i in stockPrice:
    print(i)
print('--------------------')