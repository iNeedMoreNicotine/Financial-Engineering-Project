from math import log, exp, sqrt
import numpy as np
import multiprocessing

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
    def __init__(self, time_elapsed, layers_prev, M, u, d, StInit, StAve, St, i, j, type):
        self.time_elapsed = time_elapsed
        self.layers_prev = layers_prev
        self.M = M
        self.u = u
        self.d = d
        self.StInit = StInit
        self.StAve = StAve
        self.St = St
        self.i = i+1
        self.j = j
        self.type = type

        self.avgMax = None
        self.avgMin = None
        self.avgLst = []
        self.payoff = []
        self.callValue = []
        self.zipped = None
        
    # calculate avgMax and avgMin
    def calc_Amax(self):
        if self.time_elapsed == 0:
            Amax = (self.StInit + self.StInit * self.u * (1-self.u**(self.i-self.j))/(1-self.u) + self.StInit * self.u**(self.i - self.j) * self.d * (1-self.d**self.j)/(1-self.d))/(self.i+1)
            self.avgMax = Amax
        else:
            Amax = (self.StAve*(self.layers_prev+1) + self.StInit * self.u * (1-self.u**(self.i-self.j))/(1-self.u) + self.StInit * self.u**(self.i - self.j) * self.d * (1-self.d**self.j)/(1-self.d))/(self.i+self.layers_prev+1)
            self.avgMax = Amax


    def calc_Amin(self):
        if self.time_elapsed == 0:
            Amin = (self.StInit + self.StInit * self.d * (1-self.d**self.j)/(1-self.d) + self.StInit * self.d**self.j * self.u * (1-self.u**(self.i - self.j))/(1-self.u))/(self.i+1)
            self.avgMin = Amin
        else:
            Amin = (self.StAve*(self.layers_prev+1) + self.StInit * self.d * (1-self.d**self.j)/(1-self.d) + self.StInit * self.d**self.j * self.u * (1-self.u**(self.i - self.j))/(1-self.u))/(self.i+self.layers_prev+1)
            self.avgMin = Amin

    # calculate representative averages
    def calc_Avg_equal(self):
        for k in range(self.M+1):
            avg = (self.M-k)/self.M * self.avgMax + k/self.M * self.avgMin
            self.avgLst.append(avg)

    def calc_Avg_log(self):
        for k in range(self.M+1):
            avg = exp((self.M-k)/self.M * log(self.avgMax) + k/self.M * log(self.avgMin))
            self.avgLst.append(avg)
    

def average_CRR(StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type):
    dt = time_left_to_maturity/layers
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    p = (exp((r-q)*dt) - d)/(u - d)

    stockPrice = []
    for i in range(2, layers+2):
        stockPrice.append([0]*i)
    for i in range(layers):
        for j in range(i+2):
            stockPrice[i][j] = StInit * u**(i+1-j) * d**(j)
    stockPrice = calibratedPrice(stockPrice, StInit, layers)

    TreeNodes = []
    for i in range(2, layers+2):
        TreeNodes.append([0]*i)
    for i in range(layers):
        for j in range(i+2):
            TreeNodes[i][j] = Tree_Node(time_elapsed, layers_prev, M, u, d, StInit, StAve, stockPrice[i][j], i, j, type)
            TreeNodes[i][j].calc_Amax()
            TreeNodes[i][j].calc_Amin()
            TreeNodes[i][j].calc_Avg_equal()