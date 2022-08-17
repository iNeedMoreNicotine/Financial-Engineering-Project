from math import log, sqrt, exp
from scipy.stats import norm

def bs(S0, K, T, r, q, sigma, call_put):
    S0 = float(S0)
    d1 = (log(S0 / K) + (r - q + 0.5 * sigma **2) * T) / sigma / sqrt(T)
    d2 = d1 - sigma * sqrt(T)
    if call_put == 'call':
        price = S0 * exp(-q * T) * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
        # return price
        return(f"(BS) Price of European {call_put} : {price}")
    else:
        price = S0 * exp(-q * T) * (norm.cdf(d1) - 1) - K * exp(-r * T) * (norm.cdf(d2) - 1)   
        # return price
        return(f"(BS) Price of European {call_put} : {price}")

S0 = 115
K = 120
r = 0.01
q = 0.02
sigma = 0.5
T = 1

testCall = bs(S0, K, T, r, q, sigma, "call")
testPut = bs(S0, K, T, r, q, sigma, "put")

print(testCall)
print(testPut)