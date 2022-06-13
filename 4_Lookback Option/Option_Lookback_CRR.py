from math import log, sqrt, exp
import bisect
import time

def simulate_calibrated_stock_price(St, u, d, layers):
    stockPrice = []
    for i in range(layers+1):
        stockPrice.append([0]*(i+1))
    for i in range(layers+1):
        for j in range(i+1):
            stockPrice[i][j] = St * u**(i-j) * d**j

    last1 = stockPrice[-1]
    last2 = stockPrice[-2]
    calibration = sorted(last1 + last2, reverse = True)
    calibration[layers] = St

    caliIndex = []
    for i in range(layers,-layers-1,-1):
        caliIndex.append(i)
    calibration = dict(zip(caliIndex, calibration))

    # indexDiff : u的次方 - d的次方
    for i in range(layers+1):
        for j in range(i+1):
            indexDiff = (i-j) - j
            stockPrice[i][j] = calibration[indexDiff]

    return stockPrice


class Tree_Node:
    def __init__(self, St):
        self.St = St
        self.SmaxLst = []
        self.payoff = []
        self.putValue = []


def lookback_CRR(StMax, St, T, r, q, sigma, layers, type):
    dt = T/layers
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    p = (exp((r-q)*dt) - d)/(u - d)

    stockPrice = simulate_calibrated_stock_price(St, u, d, layers)

    # 建立節點
    TreeNodes = []
    for i in range(layers+1):
        TreeNodes.append([0]* (i+1))
    for i in range(layers+1):
        for j in range(i+1):
            TreeNodes[i][j] = Tree_Node(stockPrice[i][j])

    # 第0個節點 (即今日)
    if StMax >= St:
        TreeNodes[0][0].SmaxLst = [StMax]
    else:
        TreeNodes[0][0].SmaxLst = [St]

    # Build Smax by forward tracking method
    for i in range(1, layers+1):
        for j in range(i+1):
            if j == 0:
                for Smax in TreeNodes[i-1][j].SmaxLst:
                    if Smax >= TreeNodes[i][j].St:
                        if Smax not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, Smax)
                    else:
                        if TreeNodes[i][j].St not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, TreeNodes[i][j].St)
            
            elif j == i:
                for Smax in TreeNodes[i-1][j-1].SmaxLst:
                    if Smax >= TreeNodes[i][j].St:
                        if Smax not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, Smax)
                    else:
                        if TreeNodes[i][j].St not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, TreeNodes[i][j].St)
            
            else:
                for Smax in TreeNodes[i-1][j-1].SmaxLst:
                    if Smax >= TreeNodes[i][j].St:
                        if Smax not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, Smax)
                    else:
                        if TreeNodes[i][j].St not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, TreeNodes[i][j].St)

                for Smax in TreeNodes[i-1][j].SmaxLst:
                    if Smax >= TreeNodes[i][j].St:
                        if Smax not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, Smax)
                    else:
                        if TreeNodes[i][j].St not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, TreeNodes[i][j].St)
            
            # 最後一層要有payoff list
            if i == layers:
                # 現在，我有Smax list
                for Smax in TreeNodes[i][j].SmaxLst:
                        TreeNodes[i][j].putValue.append(max(Smax-TreeNodes[i][j].St, 0))

    # Backward induction
    times = 0
    i_temp = layers - 1
    while times < layers:
        for j in range(i_temp+1):
            ku, kd = 0, 0
            for Smax in TreeNodes[i_temp][j].SmaxLst:
                u_is_found = False
                # search for ku in the SmaxLst of the upper node in next layer
                # search for self
                for k in range(ku, len(TreeNodes[i_temp+1][j].SmaxLst)):
                    if TreeNodes[i_temp+1][j].SmaxLst[k] == Smax:
                        ku = k
                        u_is_found = True
                        break
                # search for self*u
                if u_is_found == False:
                    for k in range(ku, len(TreeNodes[i_temp+1][j].SmaxLst)):
                        if abs(TreeNodes[i_temp+1][j].SmaxLst[k] - Smax*u) < 10**-8:
                            ku = k
                            break

                # search for kd in the SmaxLst of the lower node in next layer
                for k in range(kd, len(TreeNodes[i_temp+1][j+1].SmaxLst)):
                    if TreeNodes[i_temp+1][j+1].SmaxLst[k] == Smax:
                        kd = k
                        break

                # using index() method
                # if Smax in TreeNodes[i_temp+1][j].SmaxLst:
                #     ku = TreeNodes[i_temp+1][j].SmaxLst.index(Smax)
                # else:
                #     for k in range(len(TreeNodes[i_temp+1][j].SmaxLst)):
                #         if abs(TreeNodes[i_temp+1][j].SmaxLst[k] - Smax) < 10**-8:
                #             ku = TreeNodes[i_temp+1][j].SmaxLst.index(Smax)
                #             break
                
                # kd = TreeNodes[i_temp+1][j+1].SmaxLst.index(Smax)

                discounted = (TreeNodes[i_temp+1][j].putValue[ku]*p + TreeNodes[i_temp+1][j+1].putValue[kd]*(1-p)) * exp(-r*dt)
                if type == 'American':
                    discounted = max(Smax - TreeNodes[i_temp][j].St, discounted)
                TreeNodes[i_temp][j].putValue.append(discounted)

        i_temp -= 1
        times += 1

    putValue = round(TreeNodes[0][0].putValue[0], 4)
    print(f'(CRR Binomial Tree) Price of {type} Lookback Put : {putValue}')
    return putValue



# main
St = 50
T = 0.25
r = 0.1
q = 0
sigma = 0.4

start = time.perf_counter()

print('============================================================')
StMax = 50
print('Lookback Option')
print(f'[ Smax,t = {StMax} ]')
print('------------------------------------------------------------')
layers = 100
print(f'n = {layers}')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'European')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'American')
print('------------------------------------------------------------')
layers = 300
print(f'n = {layers}')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'European')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'American')
print()

print('============================================================')
StMax = 60
print('Lookback Option')
print(f'[ Smax,t = {StMax} ]')
print('------------------------------------------------------------')
layers = 100
print(f'n = {layers}')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'European')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'American')
print('------------------------------------------------------------')
layers = 300
print(f'n = {layers}')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'European')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'American')
print()

print('============================================================')
StMax = 70
print('Lookback Option')
print(f'[ Smax,t = {StMax} ]')
print('------------------------------------------------------------')
layers = 100
print(f'n = {layers}')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'European')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'American')
print('------------------------------------------------------------')
layers = 300
print(f'n = {layers}')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'European')
lookback_CRR(StMax, St, T, r, q, sigma, layers, 'American')
print()

finish = time.perf_counter()
print(f'Process finished in {round(finish - start, 2)} second(s).')
print('\n')