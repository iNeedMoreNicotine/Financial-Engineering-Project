from math import log, exp, sqrt
import numpy as np
import matplotlib.pyplot as plt
import threading
# payoff = max(Smax,τ − Sτ , 0)

def lookback_MC(StMax, St, T, r, q, sigma, n, sims, reps):
    dt = T/n
    times = 0
    means = []
    while times < reps:
        putValues = []
        for sim in range(sims):
            logSmax = log(StMax)
            stockPrices = [log(St) + (r-q-sigma**2/2)*dt + sigma*sqrt(dt)*np.random.standard_normal()]
            for i in range(1, n):
                dlnS = (r-q-sigma**2/2)*dt + sigma*sqrt(dt)*np.random.standard_normal()
                price = dlnS + stockPrices[i-1]
                stockPrices.append(price)

                if price > logSmax:
                    logSmax = price

            # 這裡才取指數
            for i in range(n):
                stockPrices[i] = exp(stockPrices[i])
            Smax = exp(logSmax)

            putValue = max(Smax - stockPrices[n-1], 0) * exp(-r * T)
            putValues.append(putValue)

        mean = np.mean(putValues)
        means.append(mean)
        times += 1

    sdOfRep = np.std(means)
    meanOfRep = np.mean(means)
    upperBound = meanOfRep + 2*sdOfRep
    upperBound = round(upperBound, 6)
    lowerBound = meanOfRep - 2*sdOfRep
    lowerBound = round(lowerBound, 6)
    bounds = [lowerBound, upperBound]
    print("==================================================")
    print(f"Lookback Option : European Put")
    print(f'[ Smax,t = {StMax} ]')
    print("--------------------")
    print(f"平均 : {round(meanOfRep, 6)}")
    print(f"標準誤 : {round(sdOfRep, 6)}")
    print(f"九十五趴信賴區間 : {bounds}")

    return meanOfRep




# main
St = 50
T = 0.25
r = 0.1
q = 0
sigma = 0.4
n = 100
sims = 10000
reps = 20

StMax = 50
lookback_MC(StMax, St, T, r, q, sigma, n, sims, reps)
StMax = 60
lookback_MC(StMax, St, T, r, q, sigma, n, sims, reps)
StMax = 70
lookback_MC(StMax, St, T, r, q, sigma, n, sims, reps)