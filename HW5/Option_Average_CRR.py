from math import log, exp, sqrt
import numpy as np
import time
import multiprocessing

# arithmetic average call
# payoff = max(Save,τ − K, 0)

# time_elapsed ------> t
# time_left_to_Maturity ------> T - t
def linear_interpolation(x, tup0, tup1):
    # tup0 = (avg0, call0)
    # tup1 = (avg1, call1)
    w = (tup1[0]-x)/(tup1[0]-tup0[0])
    result = w*tup0[1] + (1-w)*tup1[1]
    return result

class Tree_Node:
    def __init__(self, time_elapsed, layers_prev, M, u, d, StInit, StAve, St, i, j, K):
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
        self.K = K

        self.avgMax = None
        self.avgMin = None
        self.avgLst = []
        self.callValue = []
        
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
    # from large to small
    def calc_Avg_equal(self):
        for k in range(self.M+1):
            avg = (self.M-k)/self.M * self.avgMax + k/self.M * self.avgMin
            self.avgLst.append(avg)

    def calc_Avg_log(self):
        for k in range(self.M+1):
            avg = exp((self.M-k)/self.M * log(self.avgMax) + k/self.M * log(self.avgMin))
            self.avgLst.append(avg)
    
    def calc_terminalPayoff(self):
        for k in range(self.M+1):
            self.callValue.append(max(self.avgLst[k] - self.K, 0))

def average_CRR(StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed = False, search_method = 'sequential'):
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

    TreeNodes = []
    for i in range(2, layers+2):
        TreeNodes.append([0]*i)
    for i in range(layers):
        for j in range(i+2):
            TreeNodes[i][j] = Tree_Node(time_elapsed, layers_prev, M, u, d, StInit, StAve, stockPrice[i][j], i, j, K)
            TreeNodes[i][j].calc_Amax()
            TreeNodes[i][j].calc_Amin()
            if log_arrayed == False:
                TreeNodes[i][j].calc_Avg_equal()
            else:
                TreeNodes[i][j].calc_Avg_log()

    # decide the payoffs of terminal nodes
    for j in range(layers+1):
        TreeNodes[layers-1][j].calc_terminalPayoff()

    # backward induction
    counter = layers
    times = 0
    while times < layers-1:
        for j in range(counter):
            for avg in TreeNodes[counter-2][j].avgLst:
                # sequential search
                if time_elapsed == 0:
                    Au = ((counter-1)*avg + StInit * u**(counter-1-j) * d**(j))/counter
                    Ad = ((counter-1)*avg + StInit * u**((counter-1)-(j+1)) * d**(j+1))/counter
                else:
                    Au = ((layers_prev+counter-1)*avg + StInit * u**(counter-1-j) * d**(j))/(layers_prev+counter)
                    Ad = ((layers_prev+counter-1)*avg + StInit * u**((counter-1)-(j+1)) * d**(j+1))/(layers_prev+counter)

                if search_method == 'sequential':
                    # search for Au
                    for m in range(len(TreeNodes[counter-1][j].avgLst)):
                        if TreeNodes[counter-1][j].avgLst[m] < avg:
                            avg0 = TreeNodes[counter-1][j].avgLst[m]
                            call0 = TreeNodes[counter-1][j].callValue[m]
                            avg1 = TreeNodes[counter-1][j].avgLst[m-1]
                            call1 = TreeNodes[counter-1][j].callValue[m-1]
                            Cu = linear_interpolation(avg, (avg0, call0), (avg1, call1))

                    # search for Ad
                    for m in range(len(TreeNodes[counter-1][j+1].avgLst)):
                        if TreeNodes[counter-1][j+1].avgLst[m] < avg:
                            avg0 = TreeNodes[counter-1][j+1].avgLst[m]
                            call0 = TreeNodes[counter-1][j+1].callValue[m]
                            avg1 = TreeNodes[counter-1][j+1].avgLst[m-1]
                            call1 = TreeNodes[counter-1][j+1].callValue[m-1]
                            Cd = linear_interpolation(avg, (avg0, call0), (avg1, call1))
                
                # elif search_method == 'binary':



                # elif search_method == 'interpolation':



                discounted = (p*Cu + (1-p)*Cd) * exp(-r*dt)
                if type == 'American':
                    xValue = avg - K
                    discounted = max(xValue, discounted)
                TreeNodes[counter-2][j].callValue.append(discounted)

        counter -= 1
        time += 1