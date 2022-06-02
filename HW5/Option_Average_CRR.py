from math import log, exp, sqrt
import numpy as np

def calibratedPrice(stockPrice, St, layers):
    last1 = stockPrice[-1]
    last2 = stockPrice[-2]
    calibration = sorted(last1 + last2, reverse = True)
    calibration[layers] = St
    caliIndex = []
    for i in range(layers,-layers-1,-1):
        caliIndex.append(i)
    calibration = dict(zip(caliIndex, calibration))

    for i in range(layers):
        for j in range(i+2):
            indexDiff = (i+1-j) - j
            stockPrice[i][j] = calibration[indexDiff]
            
    return stockPrice

class Tree_Node:
    def __init__(self, St):
        self.St = St
        self.averageLst = []
        self.payoff = []
        self.callValue = []
        self.zipped = None


def average_CRR(St_ave, St, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, n):
    dt = time_left_to_maturity/n
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    p = (exp((r-q)*dt) - d)/(u - d)