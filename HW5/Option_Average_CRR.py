from math import log, exp, sqrt
import numpy as np
import time
import multiprocessing

# arithmetic average call
# payoff = max(Save,τ − K, 0)

# time_elapsed ------> t
# time_left_to_Maturity ------> T - t

def simulate_stock_price(StInit, u, d,layers):
    stockPrice = []
    for i in range(2, layers+2):
        stockPrice.append([0]*i)
    for i in range(layers):
        for j in range(i+2):
            stockPrice[i][j] = StInit * u**(i+1-j) * d**(j)
    stockPrice.insert(0, [StInit])

    return stockPrice

class Tree_Node:
    def __init__(self, StAve, StInit, St, K, u, d, i, j, time_elapsed, layers_prev, M):
        self.StAve = StAve
        self.StInit = StInit
        self.St = St
        self.K = K
        self.u = u
        self.d = d
        self.i = i
        self.j = j
        self.time_elapsed = time_elapsed
        self.layers_prev = layers_prev
        self.M = M
        self.avgMax = None
        self.avgMin = None
        self.avgLst = []
        self.callValue = []

    def calc_avgMax(self):
        if self.time_elapsed == 0:
            avgMax = (self.StInit + self.StInit*(self.u*(1-self.u**(self.i-self.j))/(1-self.u) + (self.u**(self.i-self.j))*self.d*(1-self.d**self.j)/(1-self.d)))/(self.i+1)
        else:
            avgMax = (self.StAve*(self.layers_prev+1) + self.StInit*(self.u*(1-self.u**(self.i-self.j))/(1-self.u) + (self.u**(self.i-self.j))*self.d*(1-self.d**self.j)/(1-self.d)))/(self.i+self.layers_prev+1)
        self.avgMax = avgMax

    def calc_avgMin(self):
        if self.j == 0 or self.j == self.i:
            self.avgMin = self.avgMax
        else:
            if self.time_elapsed == 0:
                avgMin = (self.StInit + self.StInit*(self.d*(1-self.d**self.j)/(1-self.d) + (self.d**self.j)*self.u*(1-self.u**(self.i-self.j))/(1-self.u)))/(self.i+1)
            else:
                avgMin = (self.StAve*(self.layers_prev+1) + self.StInit*(self.d*(1-self.d**self.j)/(1-self.d) + (self.d**self.j)*self.u*(1-self.u**(self.i-self.j))/(1-self.u)))/(self.i+self.layers_prev+1)
            self.avgMin = avgMin
    
    def calc_avg_equal(self):
        if self.j == 0 or self.j == self.i:
            self.avgLst.append(self.avgMax)
        else:
            for k in range(self.M+1):
                avg = self.avgMax*(self.M-k)/self.M + self.avgMin*k/self.M
                self.avgLst.append(avg)

    def calc_avg_log(self):
        if self.j == 0 or self.j == self.i:
            self.avgLst.append(self.avgMax)
        else:
            for k in range(self.M+1):
                avg = exp(log(self.avgMax)*(self.M-k)/self.M + log(self.avgMin)*k/self.M)
                self.avgLst.append(avg)

    def calc_payoff(self):
        for k in range(len(self.avgLst)):
            self.callValue.append(max(self.avgLst[k]-self.K, 0))


def average_CRR(StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed):
    dt = time_left_to_maturity/layers
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    p = (exp((r-q)*dt) - d)/(u - d)
    stockPrice = simulate_stock_price(StInit, u, d, layers)
    # print(stockPrice)

    TreeNodes = []
    for i in range(layers+1):
        TreeNodes.append([0]*(i+1))
    # print(TreeNodes)

    for i in range(layers+1):
        for j in range(i+1):
            TreeNodes[i][j] = Tree_Node(StAve, StInit, stockPrice[i][j], K, u, d, i, j, time_elapsed, layers_prev, M)
            TreeNodes[i][j].calc_avgMax()
            TreeNodes[i][j].calc_avgMin()
            if log_arrayed == False:
                TreeNodes[i][j].calc_avg_equal()
            else:
                TreeNodes[i][j].calc_avg_log()
    
    # calculate terminal payoff
    for j in range(layers+1):
        TreeNodes[layers][j].calc_payoff()

    # backward induction
    times = 0
    i_temp = layers-1
    # for each layer
    while True:
        # node(0, 0)
        if i_temp == 0:
            # only one possible Cu and Cd at node(0, 0)
            Cu = TreeNodes[i_temp+1][0].callValue[0]
            Cd = TreeNodes[i_temp+1][1].callValue[0]
            discounted = (p*Cu + (1-p)*Cd) * exp(-r*dt)
            if type == 'American':
                xValue = StAve - K
                discounted = max(xValue, discounted)
            TreeNodes[i_temp][0].callValue.append(discounted)
            break
        
        else:
            # for each node
            for j in range(i_temp+1):
                # for each avg in avgLst of the node
                if j == 0:
                    # only need to find Cd
                    Cu = TreeNodes[i_temp+1][j].callValue[0]
                    avg = TreeNodes[i_temp+1][j].avgLst[0]
                    Ad = (avg*(i_temp+1) + StInit*(u**(i_temp-j))*d**(j+1))/(i_temp+2)

                    Cd = 0
                    for kd in range(len(TreeNodes[i_temp+1][j+1].avgLst)):
                        if abs(TreeNodes[i_temp+1][j+1].avgLst[kd] - Ad) > 10**-8 and TreeNodes[i_temp+1][j+1].avgLst[kd] < Ad:
                            wd = (TreeNodes[i_temp+1][j+1].avgLst[kd-1] - Ad)/(TreeNodes[i_temp+1][j+1].avgLst[kd-1] - TreeNodes[i_temp+1][j+1].avgLst[kd])
                            Cd = wd*TreeNodes[i_temp+1][j+1].callValue[kd] + (1-wd)*TreeNodes[i_temp+1][j+1].callValue[kd-1]
                            break

                    discounted = (p*Cu + (1-p)*Cd) * exp(-r*dt)
                    if type == 'American':
                        xValue = StAve - K
                        discounted = max(xValue, discounted)
                    TreeNodes[i_temp][j].callValue.append(discounted)

                elif j ==  i_temp:
                    # only need to find Cu
                    Cd = TreeNodes[i_temp+1][j+1].callValue[0]
                    avg = TreeNodes[i_temp+1][j].avgLst[0]
                    Au = (avg*(i_temp+1) + StInit*(u**(i_temp+1-j))*d**j)/(i_temp+2)

                    Cu = 0
                    for ku in range(len(TreeNodes[i_temp+1][j].avgLst)):
                        if abs(TreeNodes[i_temp+1][j].avgLst[ku] - Au) > 10**-8 and TreeNodes[i_temp+1][j].avgLst[ku] < Au:
                            wu = (TreeNodes[i_temp+1][j].avgLst[ku-1] - Au)/(TreeNodes[i_temp+1][j].avgLst[ku-1] - TreeNodes[i_temp+1][j].avgLst[ku])
                            Cu = wu*TreeNodes[i_temp+1][j].callValue[ku] + (1-wu)*TreeNodes[i_temp+1][j].callValue[ku-1]
                            break

                    discounted = (p*Cu + (1-p)*Cd) * exp(-r*dt)
                    if type == 'American':
                        xValue = StAve - K
                        discounted = max(xValue, discounted)
                    TreeNodes[i_temp][j].callValue.append(discounted)

                else:
                    for avg in TreeNodes[i_temp][j].avgLst:
                        if time_elapsed == 0:
                            Au = (avg*(i_temp+1) + StInit*(u**(i_temp+1-j))*d**j)/(i_temp+2)
                            Ad = (avg*(i_temp+1) + StInit*(u**(i_temp-j))*d**(j+1))/(i_temp+2)
                        else:
                            Au = (avg*(layers_prev+i_temp+1) + StInit*(u**(i_temp+1-j))*d**j)/(layers_prev+i_temp+2)
                            Ad = (avg*(layers_prev+i_temp+1) + StInit*(u**(i_temp-j))*d**(j+1))/(layers_prev+i_temp+2)
                        
                        Cu, Cd = 0, 0
                        # search for Au, get Cu by interpolation
                        for ku in range(len(TreeNodes[i_temp+1][j].avgLst)):
                            if abs(TreeNodes[i_temp+1][j].avgLst[ku] - Au) > 10**-8 and TreeNodes[i_temp+1][j].avgLst[ku] < Au:
                                wu = (TreeNodes[i_temp+1][j].avgLst[ku-1] - Au)/(TreeNodes[i_temp+1][j].avgLst[ku-1] - TreeNodes[i_temp+1][j].avgLst[ku])
                                Cu = wu*TreeNodes[i_temp+1][j].callValue[ku] + (1-wu)*TreeNodes[i_temp+1][j].callValue[ku-1]
                                break

                        # search for Ad, get Cd by interpolation
                        for kd in range(len(TreeNodes[i_temp+1][j+1].avgLst)):
                            if abs(TreeNodes[i_temp+1][j+1].avgLst[kd] - Ad) > 10**-8 and TreeNodes[i_temp+1][j+1].avgLst[kd] < Ad:
                                wd = (TreeNodes[i_temp+1][j+1].avgLst[kd-1] - Ad)/(TreeNodes[i_temp+1][j+1].avgLst[kd-1] - TreeNodes[i_temp+1][j+1].avgLst[kd])
                                Cd = wd*TreeNodes[i_temp+1][j+1].callValue[kd] + (1-wd)*TreeNodes[i_temp+1][j+1].callValue[kd-1]
                                break
                        
                        discounted = (p*Cu + (1-p)*Cd) * exp(-r*dt)
                        if type == 'American':
                            xValue = StAve - K
                            discounted = max(xValue, discounted)
                        TreeNodes[i_temp][j].callValue.append(discounted)

            i_temp -= 1
    
    print('============================================================')
    if time_elapsed == 0:
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} ]')
    else:
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} | previous layers = {layers_prev} ]')
    print(f'log arrayed = {log_arrayed}')
    print('------------------------------------------------------------')
    print(f'(CRR Binomial Tree) Price of {type} Average Call : {round(TreeNodes[0][0].callValue[0], 4)}')
    print()
    return TreeNodes[0][0].callValue[0]

# main
StInit = 50
StAve = 50
K = 50
r = 0.1
q = 0.05
sigma = 0.8
time_left_to_maturity = 0.25
M = 2
layers_prev = 100
layers = 100

type = 'European'
time_elapsed = 0
log_arrayed = False
average_CRR(StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed)
log_arrayed = True
average_CRR(StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed)


# start = time.perf_counter()
# if __name__ == '__main__':
#     log_arrayed = False

#     type = 'European'
#     time_elapsed = 0
#     p1 = multiprocessing.Process(target = average_CRR, 
#                                  args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed])
#     time_elapsed = 0.25
#     p2 = multiprocessing.Process(target = average_CRR, 
#                                  args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed])
    
#     log_arrayed = True
#     time_elapsed = 0
#     p3 = multiprocessing.Process(target = average_CRR, 
#                                  args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed])
#     time_elapsed = 0.25
#     p4 = multiprocessing.Process(target = average_CRR, 
#                                  args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed])


#     type = 'American'
#     time_elapsed = 0
#     p5 = multiprocessing.Process(target = average_CRR, 
#                                  args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed])
#     time_elapsed = 0.25
#     p6 = multiprocessing.Process(target = average_CRR, 
#                                  args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed])
    
#     log_arrayed = True
#     time_elapsed = 0
#     p7 = multiprocessing.Process(target = average_CRR, 
#                                  args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed])
#     time_elapsed = 0.25
#     p8 = multiprocessing.Process(target = average_CRR, 
#                                  args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type, log_arrayed])

#     processes = [p1, p2, p3, p4, p5, p6, p7, p8]
#     for process in processes:
#         process.start()
#     for process in processes:
#         process.join()

#     finish = time.perf_counter()
#     print("============================================================")
#     print(f'Process finished in {round(finish - start, 2)} second(s).')