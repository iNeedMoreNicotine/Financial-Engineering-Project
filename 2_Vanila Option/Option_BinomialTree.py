# http://www.math.columbia.edu/~smirnov/options13.html
from math import log, sqrt, exp
# from scipy.stats import binom

def binomial_prob(n, j, p):
    # n!/j!
    temp1 = []
    for i in range(n-j):
        temp1.append(n-i)
    
    # (n-j)!
    temp2 = []
    for i in range(1, n-j+1):
        temp2.append(i)
    
    # 取ln
    for i in range(len(temp1)):
        temp1[i] = log(temp1[i])
    sum1 = sum(temp1)
    for i in range(len(temp2)):
        temp2[i] = log(temp2[i])
    sum2 = sum(temp2)

    sumTerms = sum1 - sum2 + (n-j)*log(p) + j*log(1-p)
    return exp(sumTerms)

def binomial_European(S0, K, T, r, q, sigma, layers, call_put):
    dt = T/layers
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    p = (exp((r-q)*dt) - d)/(u - d)

    stockPrice = []
    for j in range(layers+1):
        stockPrice.append(S0 * u**(layers-j) * d**(j))
        
    if call_put == "call":
        # 計算call價格
        callPrice = []
        for i in range(layers+1):
            callPrice.append(max(stockPrice[i]-K, 0))
        # 一般的方法
        times = 0
        while times < layers:
            for i in range(len(callPrice)-1):
                callPrice[i] = (callPrice[i]*p + callPrice[i+1]*(1-p)) * exp(-r*dt)
            callPrice.pop()
            times += 1
        callPrice[0] = round(callPrice[0], 6)

        return(f"(CRR Binomial Tree) Price of European {call_put} : {callPrice[0]}")
    
    else:
        # 計算put價格
        putPrice = []
        for i in range(layers+1):
            putPrice.append(max(K-stockPrice[i], 0))
        times = 0
        while times < layers:
            for i in range(len(putPrice)-1):
                putPrice[i] = (putPrice[i]*p + putPrice[i+1]*(1-p)) * exp(-r*dt)
            putPrice.pop()
            times += 1
        putPrice[0] = round(putPrice[0], 6)

        return(f"(CRR Binomial Tree) Price of European {call_put} : {putPrice[0]}")

def binomial_American(S0, K, T, r, q, sigma, layers, call_put):
    dt = T/layers
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    p = (exp((r-q)*dt) - d)/(u - d)

    # 美式選擇權每個節點之價值：max(選擇權價格, 提前履約所得之價值)
    stockPrice = []
    for i in range(2, layers+2):
        stockPrice.append([0]*i)

    for i in range(layers):
        for j in range(i+2):
            stockPrice[i][j] = S0 * u**(i+1-j) * d**(j)

    if call_put == "call":
        counter = layers
        times = 0
        callPrice = [0] * (layers+1)
        while times < layers - 1:
            # 從最後一期開始算call price
            if times == 0:
                for j in range(len(stockPrice[counter-1])):
                    callPrice[j] = max(stockPrice[counter-1][j]-K, 0)
            
            # 計算該期前一期的call price
            for j in range(len(callPrice)-1):
                callPrice[j] = (callPrice[j] * p + callPrice[j+1] * (1-p)) * exp(-r*dt)
            # 把最後一項打掉
            callPrice.pop()

            # 搞一個履約價值的list
            xValue = []
            for j in range(len(stockPrice[counter-2])):
                xValue.append(max(stockPrice[counter-2][j]-K, 0))

            for j in range(len(callPrice)):
                callPrice[j] = max(callPrice[j], xValue[j])

            counter -= 1
            times += 1

        # 迴圈跑完後，得第一期的callPrice[x, y]
        callPrice = (callPrice[0] * p + callPrice[1] * (1-p)) * exp(-r*dt)
        americanCall = max(callPrice, S0-K)
        americanCall = round(americanCall, 6)

        return(f"(CRR Binomial Tree) Price of American {call_put} : {americanCall}")

    else:
        counter = layers
        times = 0
        putPrice = [0] * (layers+1)
        while times < layers - 1:
            # 從最後一期開始算put price
            if times == 0:
                for j in range(len(stockPrice[counter-1])):
                    putPrice[j] = max(K-stockPrice[counter-1][j], 0)

            # 計算該期前一期的put price
            for j in range(len(putPrice)-1):
                putPrice[j] = (putPrice[j] * p + putPrice[j+1] * (1-p)) * exp(-r*dt)
            # 把最後一項打掉
            putPrice.pop()

            # 搞一個履約價值的list
            xValue = []
            for j in range(len(stockPrice[counter-2])):
                xValue.append(max(K-stockPrice[counter-2][j], 0))

            for j in range(len(putPrice)):
                putPrice[j] = max(putPrice[j], xValue[j])

            counter -= 1
            times += 1

        # 迴圈跑完後，得第一期的putPrice[x, y]
        putPrice = (putPrice[0] * p + putPrice[1] * (1-p)) * exp(-r*dt)
        americanPut = max(putPrice, K-S0)
        americanPut = round(americanPut, 6)

        return(f"(CRR Binomial Tree) Price of American {call_put} : {americanPut}")

def combinatorial_European(S0, K, T, r, q, sigma, layers, call_put):
    dt = T/layers
    u = exp(sigma * sqrt(dt))
    d = exp(-sigma * sqrt(dt))
    p = (exp((r-q)*dt) - d)/(u - d)
    stockPrices = []
    for i in range(layers+1):
        stockPrices.append(S0*(u**(layers-i))*(d**i))
    if call_put == 'call':
        callPrices = []
        for i in range(layers+1):
            callPrices.append(binomial_prob(layers, i, p)*max(stockPrices[i]-K, 0))
        callValue = exp(-r * T) * sum(callPrices)
        callValue = round(callValue, 6)
        return(f"(CRR Binomial Tree) Price of European {call_put} : {callValue} (Combinatorial method)")

    elif call_put == 'put':
        putPrices = []
        for i in range(layers+1):
            putPrices.append(binomial_prob(layers, i, p)*max(K-stockPrices[i], 0))
        putValue = exp(-r * T) * sum(putPrices)
        putValue = round(putValue, 6)
        return(f"(CRR Binomial Tree) Price of European {call_put} : {putValue} (Combinatorial method)")


# main
S0 = 50
K = 50
r = 0.1
q = 0.05
sigma = 0.4
T = 0.5

# n = 100 (layers = 100)
layers = 100
# European Call
print("============================================================")
print(f'n = {layers}')
testECall = binomial_European(S0, K, T, r, q, sigma, layers, "call")
print(testECall)
# American Call
testACall = binomial_American(S0, K, T, r, q, sigma, layers, "call")
print(testACall)
# European Put
testEPut = binomial_European(S0, K, T, r, q, sigma, layers, "put")
print(testEPut)
# American Put
testAPut = binomial_American(S0, K, T, r, q, sigma, layers, "put")
print(testAPut)

# n = 500 (layers = 500)
layers = 500
# European Call
print("============================================================")
print(f'n = {layers}')
testECall = binomial_European(S0, K, T, r, q, sigma, layers, "call")
print(testECall)
# American Call
testACall = binomial_American(S0, K, T, r, q, sigma, layers, "call")
print(testACall)
# European Put
testEPut = binomial_European(S0, K, T, r, q, sigma, layers, "put")
print(testEPut)
# American Put
testAPut = binomial_American(S0, K, T, r, q, sigma, layers, "put")
print(testAPut)

# n = 1000
layers = 1000
# European Call
print("============================================================")
print(f'n = {layers}')
testECall = binomial_European(S0, K, T, r, q, sigma, layers, "call")
print(testECall)
# American Call
testACall = binomial_American(S0, K, T, r, q, sigma, layers, "call")
print(testACall)
# European Put
testEPut = binomial_European(S0, K, T, r, q, sigma, layers, "put")
print(testEPut)
# American Put
testAPut = binomial_American(S0, K, T, r, q, sigma, layers, "put")
print(testAPut)

# n = 2000
layers = 2000
# European Call
print("============================================================")
print(f'n = {layers}')
testECall = binomial_European(S0, K, T, r, q, sigma, layers, "call")
print(testECall)
# American Call
testACall = binomial_American(S0, K, T, r, q, sigma, layers, "call")
print(testACall)
# European Put
testEPut = binomial_European(S0, K, T, r, q, sigma, layers, "put")
print(testEPut)
# American Put
testAPut = binomial_American(S0, K, T, r, q, sigma, layers, "put")
print(testAPut)

# n = 3000
layers = 3000
# European Call
print("============================================================")
print(f'n = {layers}')
testECall = binomial_European(S0, K, T, r, q, sigma, layers, "call")
print(testECall)
# American Call
testACall = binomial_American(S0, K, T, r, q, sigma, layers, "call")
print(testACall)
# European Put
testEPut = binomial_European(S0, K, T, r, q, sigma, layers, "put")
print(testEPut)
# American Put
testAPut = binomial_American(S0, K, T, r, q, sigma, layers, "put")
print(testAPut)

# Combinatorial Method
layers = 10000
# European Call
print("============================================================")
print(f'n = {layers}')
testECall = combinatorial_European(S0, K, T, r, q, sigma, layers, 'call')
print(testECall)
testEPut = combinatorial_European(S0, K, T, r, q, sigma, layers, 'put')
print(testEPut)