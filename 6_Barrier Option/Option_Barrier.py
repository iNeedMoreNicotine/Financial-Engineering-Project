from math import log, exp, sqrt
import numpy as np


'''
Barrier Options:
Call:
(1) up-and-out call
(2) down-and-out call
(3) up-and-in call
(4) down-and-in call

Put:
(1) up-and-out put
(2) down-and-out put
(3) up-and-in put
(4) down-and-in put
'''


def barrier_MC(St, K, B, time_left_to_maturity, r, q, sigma, n, sims, rep, barrier_type, call_put):
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

            if call_put == 'call':
                payoff = max(stockPrices[-1] - K, 0) * exp(-r * time_left_to_maturity)
            else:
                payoff = max(K - stockPrices[-1], 0) * exp(-r * time_left_to_maturity)

            # knock-out
            if barrier_type == 'up-and-out':
                if max(stockPrices) >= B:
                    optionValues[sim] = 0
                else:
                    optionValues[sim] = payoff

            elif barrier_type == 'down-and-out':
                if min(stockPrices) <= B:
                    optionValues[sim] = 0
                else:
                    optionValues[sim] = payoff
                    
            # knock-in
            elif barrier_type == 'up-and-in':
                if max(stockPrices) >= B:
                    optionValues[sim] = payoff
                else:
                    optionValues[sim] = 0

            else:
                if min(stockPrices) <= B:
                    optionValues[sim] = payoff
                else:
                    optionValues[sim] = 0

        mean = np.mean(optionValues)
        means[times] = mean
        times += 1
    
    sdOfRep = np.std(means)
    meanOfRep = np.mean(means)
    upperBound = meanOfRep + 2*sdOfRep
    upperBound = round(upperBound, 4)
    lowerBound = meanOfRep - 2*sdOfRep
    lowerBound = round(lowerBound, 4)
    bounds = [lowerBound, upperBound]
    print('==================================================')
    print(f'Barrier Option ({barrier_type}) : European {call_put}')
    print('==================================================')
    print(f'[ B = {B} ]')
    print('--------------------------------------------------')
    print(f'Mean : {round(meanOfRep, 4)}')
    print(f'Standard Error : {round(sdOfRep, 4)}')
    print(f'95% C.I. : {bounds}')
    print()

    return meanOfRep




# main
St = 100
K = 100
time_left_to_maturity = 0.5
r = 0.02
q = 0.05
sigma = 0.4
n = 125
sims = 10000
rep = 20

B = 120
barrier_MC(St, K, B, time_left_to_maturity, r, q, sigma, n, sims, rep, 'up-and-out', 'call')
barrier_MC(St, K, B, time_left_to_maturity, r, q, sigma, n, sims, rep, 'up-and-in', 'call')

B = 80
barrier_MC(St, K, B, time_left_to_maturity, r, q, sigma, n, sims, rep, 'down-and-out', 'put')
barrier_MC(St, K, B, time_left_to_maturity, r, q, sigma, n, sims, rep, 'down-and-in', 'put')