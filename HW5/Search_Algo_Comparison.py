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

def binary_search(array, x, low, high):
    # using recursive method
    # low and high are indicies
    if high >= low:
        mid = low + (high-low)//2
        # if found at mid, return
        if abs(array[mid] - x) < 10**-8:
            return mid
    
        elif array[mid] < x and array[mid-1] > x:
            return mid

        # lower part
        elif array[mid] < x:
            return binary_search(array, x, low, mid-1)
        
        # upper part
        elif array[mid] > x:
            return binary_search(array, x, mid+1, high)

def interpolation_search(array, x, low, high):
    if high >= low:
        if high == low:
            return 0
        
        pos = ((array[low]-x)*high + (x-array[high])*low)/(array[low] - array[high])
        pos = int(pos)

        counts = 0
        while True:
            if abs(array[pos] - x) < 10**-8:
                return pos
            
            elif array[pos] < x and array[pos-1] > x:
                return pos

            else:
                if counts < 0:
                    counts -= 1
                else:
                    counts += 1
                counts = -counts
                pos = pos + counts

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

def average_CRR(StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type):
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
            TreeNodes[i][j].calc_avg_equal()
    
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
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} | Sequential Search ]')
    else:
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} | previous layers = {layers_prev} | Sequential Search ]')
    print('------------------------------------------------------------')
    print(f'(CRR Binomial Tree) Price of {type} Average Call : {round(TreeNodes[0][0].callValue[0], 4)}')
    print()
    return TreeNodes[0][0].callValue[0]

def average_CRR_binary(StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type):
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
            TreeNodes[i][j].calc_avg_equal()
    
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
                    ku = binary_search(TreeNodes[i_temp+1][j].avgLst, Au, 0, len(TreeNodes[i_temp+1][j].avgLst)-1)
                    if abs(Au - TreeNodes[i_temp+1][j].avgLst[ku]) < 10**-8:
                        Cu = TreeNodes[i_temp+1][j].callValue[ku]
                    else:
                        wu = (TreeNodes[i_temp+1][j].avgLst[ku-1] - Au)/(TreeNodes[i_temp+1][j].avgLst[ku-1] - TreeNodes[i_temp+1][j].avgLst[ku])
                        Cu = wu*TreeNodes[i_temp+1][j].callValue[ku] + (1-wu)*TreeNodes[i_temp+1][j].callValue[ku-1]

                    # search for Ad
                    kd = binary_search(TreeNodes[i_temp+1][j+1].avgLst, Ad, 0, len(TreeNodes[i_temp+1][j+1].avgLst)-1)
                    if abs(Ad - TreeNodes[i_temp+1][j+1].avgLst[kd]) < 10**-8:
                        Cd = TreeNodes[i_temp+1][j+1].callValue[kd]
                    else:
                        wd = (TreeNodes[i_temp+1][j+1].avgLst[kd-1] - Ad)/(TreeNodes[i_temp+1][j+1].avgLst[kd-1] - TreeNodes[i_temp+1][j+1].avgLst[kd])
                        Cd = wd*TreeNodes[i_temp+1][j+1].callValue[kd] + (1-wd)*TreeNodes[i_temp+1][j+1].callValue[kd-1]
                    
                    discounted = (p*Cu + (1-p)*Cd) * exp(-r*dt)
                    if type == 'American':
                        xValue = avg - K
                        discounted = max(xValue, discounted)
                    TreeNodes[i_temp][j].callValue.append(discounted)

            i_temp -= 1
    
    print('============================================================')
    if time_elapsed == 0:
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} | Binary Search ]')
    else:
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} | previous layers = {layers_prev} | Binary Search ]')
    print('------------------------------------------------------------')
    print(f'(CRR Binomial Tree) Price of {type} Average Call : {round(TreeNodes[0][0].callValue[0], 4)}')
    print()
    return TreeNodes[0][0].callValue[0]

def average_CRR_interpolation(StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type):
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
            TreeNodes[i][j].calc_avg_equal()
    
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
                    ku = interpolation_search(TreeNodes[i_temp+1][j].avgLst, Au, 0, len(TreeNodes[i_temp+1][j].avgLst)-1)
                    # ku = binary_search(TreeNodes[i_temp+1][j].avgLst, Au, 0, len(TreeNodes[i_temp+1][j].avgLst)-1)
                    if abs(Au - TreeNodes[i_temp+1][j].avgLst[ku]) < 10**-8:
                        Cu = TreeNodes[i_temp+1][j].callValue[ku]
                    else:
                        wu = (TreeNodes[i_temp+1][j].avgLst[ku-1] - Au)/(TreeNodes[i_temp+1][j].avgLst[ku-1] - TreeNodes[i_temp+1][j].avgLst[ku])
                        Cu = wu*TreeNodes[i_temp+1][j].callValue[ku] + (1-wu)*TreeNodes[i_temp+1][j].callValue[ku-1]

                    # search for Ad
                    kd = interpolation_search(TreeNodes[i_temp+1][j+1].avgLst, Ad, 0, len(TreeNodes[i_temp+1][j+1].avgLst)-1)
                    # kd = binary_search(TreeNodes[i_temp+1][j+1].avgLst, Ad, 0, len(TreeNodes[i_temp+1][j+1].avgLst)-1)
                    if abs(Ad - TreeNodes[i_temp+1][j+1].avgLst[kd]) < 10**-8:
                        Cd = TreeNodes[i_temp+1][j+1].callValue[kd]
                    else:
                        wd = (TreeNodes[i_temp+1][j+1].avgLst[kd-1] - Ad)/(TreeNodes[i_temp+1][j+1].avgLst[kd-1] - TreeNodes[i_temp+1][j+1].avgLst[kd])
                        Cd = wd*TreeNodes[i_temp+1][j+1].callValue[kd] + (1-wd)*TreeNodes[i_temp+1][j+1].callValue[kd-1]
                    
                    discounted = (p*Cu + (1-p)*Cd) * exp(-r*dt)
                    if type == 'American':
                        xValue = avg - K
                        discounted = max(xValue, discounted)
                    TreeNodes[i_temp][j].callValue.append(discounted)

            i_temp -= 1
    
    print('============================================================')
    if time_elapsed == 0:
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} | Interpolation Search ]')
    else:
        print(f'[ Save,t = {StAve} | time elapsed = {time_elapsed} | previous layers = {layers_prev} | Binary Search ]')
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
M = 750
layers_prev = 100
layers = 100

if __name__ == '__main__':
    # sequential search
    start = time.perf_counter()

    print('============================================================')
    print('{ Sequential Search }')
    time_elapsed = 0
    type = 'European'
    p1 = multiprocessing.Process(target = average_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p2 = multiprocessing.Process(target = average_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    time_elapsed = 0.25
    type = 'European'
    p3 = multiprocessing.Process(target = average_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p4 = multiprocessing.Process(target = average_CRR, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    processes = [p1, p2, p3, p4]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Process finished in {round(finish - start, 2)} second(s).')
    print('\n')


    # binary search
    start = time.perf_counter()

    print('============================================================')
    print('{ Binary Search }')
    time_elapsed = 0
    type = 'European'
    p5 = multiprocessing.Process(target = average_CRR_binary, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p6 = multiprocessing.Process(target = average_CRR_binary, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    time_elapsed = 0.25
    type = 'European'
    p7 = multiprocessing.Process(target = average_CRR_binary, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p8 = multiprocessing.Process(target = average_CRR_binary, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    processes = [p5, p6, p7, p8]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    
    finish = time.perf_counter()
    print(f'Process finished in {round(finish - start, 2)} second(s).')
    print('\n')


    # interpolation search
    start = time.perf_counter()

    print('============================================================')
    print('{ Interpolation Search }')
    time_elapsed = 0
    time_elapsed = 0
    type = 'European'
    p9 = multiprocessing.Process(target = average_CRR_interpolation, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p10 = multiprocessing.Process(target = average_CRR_interpolation, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    time_elapsed = 0.25
    type = 'European'
    p11 = multiprocessing.Process(target = average_CRR_interpolation, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])
    type = 'American'
    p12 = multiprocessing.Process(target = average_CRR_interpolation, args = [StAve, StInit, K, time_elapsed, time_left_to_maturity, r, q, sigma, M, layers_prev, layers, type])

    processes = [p9, p10, p11, p12]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Process finished in {round(finish - start, 2)} second(s).')
    print('\n')