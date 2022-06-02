# Monte Carlo
from math import log, exp, sqrt
from scipy.stats import norm
import numpy as np

S0 = float(input("S0: "))
K = input("K1~K4(以逗號隔開): ").split(",")
for i in range(len(K)):
  K[i] = float(K[i])
K1 = K[0]
K2 = K[1]
K3 = K[2]
K4 = K[3]
r = float(input("r: "))
q = float(input("q: "))
sigma = float(input("standard deviation: "))
T = float(input("T: "))

meanValueLst = []
times = 0

stockSamples = []
while times < 20:
    for i in range(100000):
        lnSample = np.random.normal(loc = log(S0) + (r - q - 0.5*(sigma**2))* T, scale = sigma * sqrt(T))
        sample = exp(lnSample)
        stockSamples.append(sample)

    optionValue = []
    for price in stockSamples:
        if K1 <= price and price < K2:
            optionValue.append(price - K1)

        elif K2 <= price and price < K3:
            optionValue.append(K2 - K1)

        elif K3 <= price and price < K4:
            optionValue.append((K2 - K1) - ((K2 - K1)/(K4 - K3)) * (price - K3))

        else:
            optionValue.append(0)
    meanValue = np.mean(optionValue)
    discounted = meanValue * exp(-r * T)
    meanValueLst.append(discounted)
    times += 1

sdOfRep = np.std(meanValueLst)
meanOfRep = np.mean(meanValueLst)
upperBound = meanOfRep + 2*sdOfRep
lowerBound = meanOfRep - 2*sdOfRep
bounds = [lowerBound, upperBound]
print("平均", end = " : ")
print(meanOfRep)
print("九十五趴信賴區間", end = " : ")
print(bounds)

# S0 = 100
# K = 90,92,94,96
# r = 0.005
# q = 0.08
# std = 0.1
# T = 1