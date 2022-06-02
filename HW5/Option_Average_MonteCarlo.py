from math import log, exp, sqrt
import numpy as np
# arithmetic average call
# payoff = max(Save,τ − K, 0)

# time_elapsed ------> t
# time_left_to_Maturity ------> T - t
def average_MC(StAve, St, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, n, sims, rep):
    dt = time_left_to_maturity/n
    times = 0
    means = []
    means = np.ndarray(shape = (rep))
    while times < rep:
        optionValues = np.ndarray(shape = (sims))

        for sim in range(sims):
            stockPrices = np.ndarray(shape = (n+1))
            stockPrices[0] = log(St)
            for i in range(n):
                dlnS = np.random.normal(loc = (r-q-sigma**2/2)*dt, scale = sigma*sqrt(dt))
                stockPrices[i+1] = dlnS
            
            stockPrices = np.cumsum(stockPrices)
            stockPrices = np.exp(stockPrices)

            if time_elapsed == 0:
                callValue = max(np.mean(stockPrices) - K, 0) * exp(-r * time_left_to_maturity)
                optionValues[sim] = callValue
            else:
                payoff = (StAve*(M + 1) + sum(stockPrices[1:]))/(M + n + 1) - K
                callValue = max(payoff, 0)
                optionValues[sim] = callValue

        mean = np.mean(optionValues)
        means[times] = mean
        times += 1

    sdOfRep = np.std(means)
    meanOfRep = np.mean(means)
    upperBound = meanOfRep + 2*sdOfRep
    upperBound = round(upperBound, 6)
    lowerBound = meanOfRep - 2*sdOfRep
    lowerBound = round(lowerBound, 6)
    bounds = [lowerBound, upperBound]
    print("============================================================")
    print(f"Average Option : European Call")
    if time_elapsed == 0:
        print(f'[ Save,t = {StAve} | time left to maturity date = {time_left_to_maturity} ]')
    else:
        print(f'[ Save,t = {StAve} | time left to maturity date = {time_left_to_maturity} | M = {M} ]')
    print("------------------------------------------------------------")
    print(f"平均 : {round(meanOfRep, 6)}")
    print(f"標準誤 : {round(sdOfRep, 6)}")
    print(f"九十五趴信賴區間 : {bounds}")

    return meanOfRep




# main
St = 50
StAve = 50
K = 50
r = 0.1
q = 0.05
sigma = 0.8
time_left_to_maturity = 0.25
sims = 10000
rep = 20
M = 100
n = 100

time_elapsed = 0
average_MC(StAve, St, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, n, sims, rep)
time_elapsed = 0.25
average_MC(StAve, St, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, n, sims, rep)