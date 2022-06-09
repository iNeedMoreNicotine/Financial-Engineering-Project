from math import log, exp, sqrt
import numpy as np
import matplotlib.pyplot as plt
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
                # for each avg in the avgLst of the node
                for avg in TreeNodes[i_temp][j].avgLst:
                    if time_elapsed == 0:
                        Au = ((i_temp+1)*avg + (StInit*u**(i_temp+1-j))*d**j)/(i_temp+2)
                        Ad = ((i_temp+1)*avg + (StInit*u**(i_temp-j))*d**(j+1))/(i_temp+2)
                    else:
                        Au = ((layers_prev+i_temp+1)*avg + (StInit*u**(i_temp+1-j))*d**j)/(layers_prev+i_temp+2)
                        Ad = ((layers_prev+i_temp+1)*avg + (StInit*u**(i_temp-j))*d**(j+1))/(layers_prev+i_temp+2)
                    
                    Cu, Cd = 0, 0
                    # search for Au
                    for avg_u in TreeNodes[i_temp+1][j].avgLst:
                        if abs(avg_u - Au) < 10**-8:
                            ku = TreeNodes[i_temp+1][j].avgLst.index(avg_u)
                            Cu = TreeNodes[i_temp+1][j].callValue[ku]
                            break
                        else:
                            if avg_u < Au:
                                ku = TreeNodes[i_temp+1][j].avgLst.index(avg_u)
                                wu = (TreeNodes[i_temp+1][j].avgLst[ku-1] - Au)/(TreeNodes[i_temp+1][j].avgLst[ku-1] - TreeNodes[i_temp+1][j].avgLst[ku])
                                Cu = wu*TreeNodes[i_temp+1][j].callValue[ku] + (1-wu)*TreeNodes[i_temp+1][j].callValue[ku-1]
                                break

                    # search for Ad
                    for avg_d in TreeNodes[i_temp+1][j+1].avgLst:
                        if abs(avg_d - Ad) < 10**-8:
                            kd = TreeNodes[i_temp+1][j+1].avgLst.index(avg_d)
                            Cd = TreeNodes[i_temp+1][j+1].callValue[kd]
                            break
                        else:
                            if avg_d < Ad:
                                kd = TreeNodes[i_temp+1][j+1].avgLst.index(avg_d)
                                wd = (TreeNodes[i_temp+1][j+1].avgLst[kd-1] - Ad)/(TreeNodes[i_temp+1][j+1].avgLst[kd-1] - TreeNodes[i_temp+1][j+1].avgLst[kd])
                                Cd = wd*TreeNodes[i_temp+1][j+1].callValue[kd] + (1-wd)*TreeNodes[i_temp+1][j+1].callValue[kd-1]
                                break
                    
                    discounted = (p*Cu + (1-p)*Cd) * exp(-r*dt)
                    if type == 'American':
                        xValue = avg - K
                        discounted = max(xValue, discounted)
                    TreeNodes[i_temp][j].callValue.append(discounted)

            i_temp -= 1
    
    print('============================================================')
    if time_elapsed == 0:
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} | M = {M}]')
    else:
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} | previous layers = {layers_prev} | M = {M}]')
    print(f'[ log arrayed = {log_arrayed} ]')
    print('------------------------------------------------------------')
    print(f'(CRR Binomial Tree) Price of {type} Average Call : {round(TreeNodes[0][0].callValue[0], 4)}')
    print()
    return TreeNodes[0][0].callValue[0]






# main
# StInit = 50
# StAve = 50
# K = 50
# r = 0.1
# q = 0.05
# sigma = 0.8
# time_elapsed = 0
# time_left_to_maturity = 0.25
# layers_prev = 100
# layers = 100

# if __name__ == '__main__':
#     start = time.perf_counter()

#     # equally-arrayed
#     type = 'European'
#     log_arrayed = False
#     processes_EU = []
#     for i in range(8):
#         p = multiprocessing.Process(target = average_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, (i+1)*50, layers_prev, layers, type, log_arrayed])
#         p.start()
#         processes_EU.append(p)

#     for process in processes_EU:
#         process.join()


#     type = 'American'
#     processes_US = []
#     for i in range(8):
#         p = multiprocessing.Process(target = average_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, (i+1)*50, layers_prev, layers, type, log_arrayed])
#         p.start()
#         processes_US.append(p)

#     for process in processes_US:
#         process.join()
    

#     # log-arrayed
#     log_arrayed = True
#     type = 'European'
#     processes_EU = []
#     for i in range(8):
#         p = multiprocessing.Process(target = average_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, (i+1)*50, layers_prev, layers, type, log_arrayed])
#         p.start()
#         processes_EU.append(p)

#     for process in processes_EU:
#         process.join()


#     type = 'American'
#     processes_US = []
#     for i in range(8):
#         p = multiprocessing.Process(target = average_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, (i+1)*50, layers_prev, layers, type, log_arrayed])
#         p.start()
#         processes_US.append(p)

#     for process in processes_US:
#         process.join()

#     finish = time.perf_counter()
#     print(f'Process finished in {round(finish - start, 2)} second(s).')



M = list(range(50, 450, 50))
print(M)

# European
equal_EU = [5.0781, 4.7354, 4.6821, 4.6652, 4.659, 4.6543, 4.6514, 4.6498]
plt.plot(M, equal_EU, color = 'green', label = 'equally-arrayed')
log_EU = [4.9278, 4.6949, 4.6699, 4.6586, 4.6531, 4.6505, 4.6488, 4.6478]
plt.plot(M, log_EU, color = 'orange', label = 'log-arrayed')

plt.xlabel('M')
plt.ylabel('Call Price')
plt.title('European Call')
plt.legend()

plt.show()

# American
equal_US = [5.7115, 5.4146, 5.3785, 5.3678, 5.3624, 5.3571, 5.3588, 5.3561]
plt.plot(M, equal_US, color = 'green', label = 'equally-arrayed')
log_US = [5.5737, 5.3904, 5.371, 5.3619, 5.3587, 5.3566, 5.3555, 5.3547]
plt.plot(M, log_US, color = 'orange', label = 'log-arrayed')

plt.xlabel('M')
plt.ylabel('Call Price')
plt.title('American Call')
plt.legend()

plt.show()