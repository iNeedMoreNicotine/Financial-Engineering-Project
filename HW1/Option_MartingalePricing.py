# Martingale Pricing
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

def calcA(ki):
    ai = (log(S0/ki) + (r - q - 0.5 * sigma**2)*T) / sigma / sqrt(T)
    return ai

def calcB(ki):
    bi = (log(S0/ki) + (r - q + 0.5 * sigma**2)*T) / sigma / sqrt(T)
    return bi

a1 = calcA(K1)
a2 = calcA(K2)
a3 = calcA(K3)
a4 = calcA(K4)
b1 = calcB(K1)
b2 = calcB(K2)
b3 = calcB(K3)
b4 = calcB(K4)

term1 = S0 * exp(-q*T) * ((norm.cdf(b1) - norm.cdf(b2)) - ((K2 - K1)/(K4 - K3)) * (norm.cdf(b3) - norm.cdf(b4)))
term2 = -exp(-r*T) * K1 * (norm.cdf(a1) - norm.cdf(a4)) + exp(-r*T) * K2 * (norm.cdf(a2) - norm.cdf(a4)) + exp(-r*T) * ((K2 - K1)/(K4 - K3)) * K3 * (norm.cdf(a3) - norm.cdf(a4))
discountedPayoff = term1 + term2
print(discountedPayoff)

# S0 = 100
# K = 90,92,94,96
# r = 0.005
# q = 0.08
# std = 0.1
# T = 1

# 🈹️🈹️🈹️ 以Black-Scholes驗算 🈹️🈹️🈹️
def BS(spot, K, T, r, q, sigma):
    spot = float(spot)
    d1 = (log(spot / K) + (r - q + 0.5 * sigma**2) * T) / sigma / sqrt(T)
    d2 = d1 - sigma * sqrt(T)
    price = spot * exp(-q*T) * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    return price
# 🈹️🈹️🈹️ 記得要調整參數 🈹️🈹️🈹️
test = BS(100, 90, 1, 0.005, 0.08, 0.1)
print(test)