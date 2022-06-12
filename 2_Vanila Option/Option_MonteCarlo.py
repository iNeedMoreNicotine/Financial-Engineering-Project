# Monte Carlo
from math import log, exp, sqrt
from scipy.stats import norm
import numpy as np

def monte_carlo_European(S0, K, r, q, sigma, T, call_put, sims, rep):
    meanValueLst = []
    times = 0

    stockSamples = []
    while times < rep:
        for i in range(sims):
            # stockSamples.append(S0 * exp((r - q - 0.5 * sigma**2) * T + sigma * sqrt(T) * np.random.standard_normal()))
            # lnSample = log(S0) + (r - q - 0.5*sigma**2) * T + sigma * sqrt(T) * np.random.standard_normal()
            lnSample = np.random.normal(loc = log(S0) + (r - q - 0.5*(sigma**2))* T, scale = sigma * sqrt(T))
            sample = exp(lnSample)
            stockSamples.append(sample)
        
        optionValue = []
        if call_put == "call":
            for price in stockSamples:
                if K <= price:
                    optionValue.append(price-K)
                else:
                    optionValue.append(0)

            meanValue = np.mean(optionValue)
            discounted = meanValue * exp(-r * T)
            meanValueLst.append(discounted)
            times += 1

        else:
            for price in stockSamples:
                if K >= price:
                    optionValue.append(K-price)
                else:
                    optionValue.append(0)

            meanValue = np.mean(optionValue)
            discounted = meanValue * exp(-r * T)
            meanValueLst.append(discounted)
            times += 1

    sdOfRep = np.std(meanValueLst)
    meanOfRep = np.mean(meanValueLst)
    upperBound = meanOfRep + 2*sdOfRep
    upperBound = round(upperBound, 6)
    lowerBound = meanOfRep - 2*sdOfRep
    lowerBound = round(lowerBound, 6)
    bounds = [lowerBound, upperBound]
    print("==================================================")
    print(f"European {call_put}")
    print("--------------------------------------------------")
    print(f"平均 : {round(meanOfRep, 6)}")
    print(f"標準誤 : {round(sdOfRep, 6)}")
    print(f"九十五趴信賴區間 : {bounds}")
    return round(meanOfRep, 6)

S0 = 115
K = 120
r = 0.01
q = 0.02
sigma = 0.5
T = 1
sims = 10000
rep = 20
monte_carlo_European(S0, K, r, q, sigma, T, "call", sims, rep)
monte_carlo_European(S0, K, r, q, sigma, T, "put", sims, rep)