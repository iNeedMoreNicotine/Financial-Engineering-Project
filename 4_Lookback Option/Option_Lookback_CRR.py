import pandas as pd
from math import log, exp, sqrt
import bisect

def calibratedPrice(stockPrice, St, layers):
    last1 = stockPrice[-1]
    last2 = stockPrice[-2]
    calibration = sorted(last1 + last2, reverse = True)
    calibration[layers] = St
    caliIndex = []
    for i in range(layers,-layers-1,-1):
        caliIndex.append(i)
    calibration = dict(zip(caliIndex,calibration))

    for i in range(layers):
        for j in range(i+2):
            indexDiff = (i+1-j) - j
            stockPrice[i][j] = calibration[indexDiff]
            
    return stockPrice

class Tree_Node:
    def __init__(self, St):
        self.St = St
        self.SmaxLst = []
        self.payoff = []
        self.putValue = []
        self.zipped = None 

def lookback_CRR(StMax, St, T, r, q, sigma, layers, type):
    dt = T/layers
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    p = (exp((r-q)*dt) - d)/(u - d)

    stockPrice = []
    for i in range(2, layers+2):
        stockPrice.append([0]*i)
    for i in range(layers):
        for j in range(i+2):
            stockPrice[i][j] = St * u**(i+1-j) * d**(j)
    # 校準股價
    stockPrice = calibratedPrice(stockPrice, St, layers)

    # 建立節點
    TreeNodes = []
    for i in range(2, layers+2):
        TreeNodes.append([0]*i)
    for i in range(layers):
        for j in range(i+2):
            TreeNodes[i][j] = Tree_Node(stockPrice[i][j])

    # 第0個節點 (即今日)
    TreeNode_0 = Tree_Node(St)
    if StMax >= St:
        TreeNode_0.SmaxLst = [StMax]
    else:
        TreeNode_0.SmaxLst = [St]

    # Build Smax by forward tracking method
    # first layer
    for j in range(2):
        if TreeNode_0.SmaxLst[0] >= TreeNodes[0][j].St:
            TreeNodes[0][j].SmaxLst.append(TreeNode_0.SmaxLst[0])
        else:
            TreeNodes[0][j].SmaxLst.append(TreeNodes[0][j].St)
    # other layers
    for i in range(1,layers):
        for j in range(i+2):
            if j == 0:
                for Smaxi in TreeNodes[i-1][j].SmaxLst:
                    if Smaxi >= TreeNodes[i][j].St:
                        if Smaxi not in TreeNodes[i][j].SmaxLst:
                            # TreeNodes[i][j].SmaxLst.append(Smaxi)
                            bisect.insort(TreeNodes[i][j].SmaxLst, Smaxi)
                    else:
                        if TreeNodes[i][j].St not in TreeNodes[i][j].SmaxLst:
                            # TreeNodes[i][j].SmaxLst.append(TreeNodes[i][j].St)
                            bisect.insort(TreeNodes[i][j].SmaxLst, TreeNodes[i][j].St)
            elif j == i+1:
                for Smaxi in TreeNodes[i-1][j-1].SmaxLst:
                    if Smaxi >= TreeNodes[i][j].St:
                        if Smaxi not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, Smaxi)
                    else:
                        if TreeNodes[i][j].St not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, TreeNodes[i][j].St)
            else:
                for Smaxi in TreeNodes[i-1][j-1].SmaxLst:
                    if Smaxi >= TreeNodes[i][j].St:
                        if Smaxi not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, Smaxi)
                    else:
                        if TreeNodes[i][j].St not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, TreeNodes[i][j].St)
                for Smaxi in TreeNodes[i-1][j].SmaxLst:
                    if Smaxi >= TreeNodes[i][j].St:
                        if Smaxi not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, Smaxi)
                    else:
                        if TreeNodes[i][j].St not in TreeNodes[i][j].SmaxLst:
                            bisect.insort(TreeNodes[i][j].SmaxLst, TreeNodes[i][j].St)
            # 最後一層要有payoff list
            if i == layers-1:
                # 現在，我有Smax list
                for Smaxi in TreeNodes[i][j].SmaxLst:
                        TreeNodes[i][j].payoff.append(max(Smaxi-TreeNodes[i][j].St, 0))
                # 然後把它zippppppp起來
                TreeNodes[i][j].zipped = list(zip(TreeNodes[i][j].SmaxLst, TreeNodes[i][j].payoff))

    # Backward induction
    # 從倒數第二層開始
    counter = layers
    times = 0
    while times < layers - 1:
        for j in range(counter):
            ku, kd = 0, 0  # indicies
            usedIndicies = []
            for Smaxi in TreeNodes[counter-2][j].SmaxLst:
                if Smaxi in TreeNodes[counter-1][j].SmaxLst:
                    ku = TreeNodes[counter-1][j].SmaxLst.index(Smaxi)
                    usedIndicies.append(ku)
                else:
                    for k in range(len(TreeNodes[counter-1][j].SmaxLst)):
                        if k in usedIndicies:
                            pass
                        else:
                            if abs(Smaxi*u - TreeNodes[counter-1][j].SmaxLst[k]) < 10**-8:
                                ku = k
                                usedIndicies.append(ku)
                                break
                kd = TreeNodes[counter-1][j+1].SmaxLst.index(Smaxi)
                usedIndicies.append(kd)

                discountedPutValue = (p * TreeNodes[counter-1][j].zipped[ku][1] + (1-p) * TreeNodes[counter-1][j+1].zipped[kd][1]) * exp(-r*dt)
                if type == 'European':
                    nodeValue = discountedPutValue
                elif type == 'American':
                    nodeValue =  max(Smaxi - TreeNodes[counter-2][j].St, discountedPutValue)
                TreeNodes[counter-2][j].putValue.append(nodeValue)
                TreeNodes[counter-2][j].zipped = list(zip(TreeNodes[counter-2][j].SmaxLst, TreeNodes[counter-2][j].putValue))
        counter -= 1
        times += 1

    # 第0個節點 (即今日)
    usedIndicies = []
    ku, kd = 0, 0
    if TreeNode_0.SmaxLst[0] in TreeNodes[0][0].SmaxLst:
        ku = TreeNodes[0][0].SmaxLst.index(TreeNode_0.SmaxLst[0])
        usedIndicies.append(ku)
    else:
        for k in range(len(TreeNodes[0][j].SmaxLst)):
            if k in usedIndicies:
                pass
            else:
                if abs(Smaxi*u - TreeNodes[0][j].SmaxLst[k]) < 10**-8:
                    ku = k
                    usedIndicies.append(ku)
                    break

    kd = TreeNodes[0][1].SmaxLst.index(TreeNode_0.SmaxLst[0])
    discountedPutValue = (p * TreeNodes[0][0].zipped[ku][1] + (1-p) * TreeNodes[0][1].zipped[kd][1]) * exp(-r*dt)
    if type == 'European':
        nodeValue = discountedPutValue
    elif type == 'American':
        nodeValue =  max(TreeNode_0.SmaxLst[0] - TreeNode_0.St, discountedPutValue)
    TreeNode_0.putValue.append(nodeValue)
    TreeNode_0.zipped = list(zip(TreeNode_0.SmaxLst, TreeNode_0.putValue))

    print(f'(CRR Binomial Tree) Price of {type} Lookback Put : {round(TreeNode_0.putValue[0], 4)}')
    return TreeNode_0.putValue[0]




# main
St = 50
T = 0.25
r = 0.1
q = 0
sigma = 0.4

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