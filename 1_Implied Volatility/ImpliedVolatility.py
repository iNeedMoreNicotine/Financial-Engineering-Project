from math import log, sqrt, exp
from scipy.stats import norm

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

def bs(S0, K, T, r, q, sigma, call_put):
    S0 = float(S0)
    d1 = (log(S0 / K) + (r - q + 0.5 * sigma **2) * T) / sigma / sqrt(T)
    d2 = d1 - sigma * sqrt(T)
    if call_put == "call":
        price = S0 * exp(-q * T) * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
        return price
    else:
        price = S0 * exp(-q * T) * (norm.cdf(d1) - 1) - K * exp(-r * T) * (norm.cdf(d2) - 1)
        return price

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
        return callPrice[0]

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
        return putPrice[0]

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
    stockPrice.insert(0, [S0])

    if call_put == "call":
        callPrice = [0] * (layers+1)
        for j in range(layers+1):
            callPrice[j] = max(stockPrice[layers][j]-K, 0)
        
        times = 0
        i_temp = layers - 1
        while times < layers:
            xValue = []
            for j in range(i_temp+1):
                callPrice[j] = (callPrice[j]*p + callPrice[j+1]*(1-p))* exp(-r*dt)
                xValue.append(max(stockPrice[i_temp][j]-K, 0))
                callPrice[j] = max(callPrice[j], xValue[j])
            
            # 把最後一項打掉
            callPrice.pop()
            i_temp -= 1
            times += 1
        
        americanCall = callPrice[0]
        return americanCall

    else:
        putPrice = [0] * (layers+1)
        for j in range(layers+1):
            putPrice[j] = max(K-stockPrice[layers][j], 0)

        times = 0
        i_temp = layers - 1
        while times < layers:
            xValue = []
            for j in range(i_temp+1):
                putPrice[j] = (putPrice[j]*p + putPrice[j+1]*(1-p))* exp(-r*dt)
                xValue.append(max(K-stockPrice[i_temp][j], 0))
                putPrice[j] = max(putPrice[j], xValue[j])
            
            # 把最後一項打掉
            putPrice.pop()
            i_temp -= 1
            times += 1

        americanPut = putPrice[0]
        return americanPut

# 定義損失函數 
def loss_function_bs(marketPrice, S0, K, T, r, q, sigma, call_put):
    return bs(S0, K, T, r, q, sigma, call_put) - marketPrice

def loss_function_binomial(marketPrice, S0, K, T, r, q, sigma, call_put, layers, type):
    if type == "European":
        return binomial_European(S0, K, T, r, q, sigma, layers, call_put) - marketPrice
    else:
        return binomial_American(S0, K, T, r, q, sigma, layers, call_put) - marketPrice

# 計算隱含波動度
# bisection method
def iv_bisection(marketPrice, S0, K, T, r, q, call_put, type, model, layers, converCrit):
    # 損失函數 < 0：市價 > BS ======> sigma應盡量取小
    # 損失函數 > 0：市價 < BS ======> sigma應盡量取大（但不要太大ㄛ）
    # 初始化區間[a, b]
    a = 0.1
    b = 1
    # 崩潰可調崩潰可調崩潰可調崩潰可調崩潰可調

    if model == "BS":
        while abs(a-b) > converCrit:
            x = a + (b-a)/2
            if loss_function_bs(marketPrice, S0, K, T, r, q, a, call_put) * loss_function_bs(marketPrice, S0, K, T, r, q, x, call_put) < 0:
                b = x
            else:
                a = x
        iv = (a + b)/2
        return iv

    elif model == "CRR":
        while abs(a-b) > converCrit:
            x = a + (b-a)/2
            if loss_function_binomial(marketPrice, S0, K, T, r, q, a, call_put, layers, type) * loss_function_binomial(marketPrice, S0, K, T, r, q, x, call_put, layers, type) < 0:
                b = x
            else:
                a = x
        iv = (a + b)/2
        return iv
    else:
        print("invalid model!!!")
        return None

# 計算導數
def vega_bs(S0, K, T, r, q, sigma):
    # put與call的vega相同 (by put-call parity)
    d1 = (log(S0 / K) + (r - q + 0.5 * sigma **2) * T) / sigma / sqrt(T)
    vega = exp(-q*T) * S0 * sqrt(T) * norm.pdf(d1)
    return vega

def vega_binomial(S0, K, T, r, q, sigma, layers, call_put, type):
    dsigma = 10**(-8)
    if type == "European":
        price0 = binomial_European(S0, K, T, r, q, sigma, layers, call_put)
        price1 = binomial_European(S0, K, T, r, q, (sigma + dsigma), layers, call_put)

    else:
        price0 = binomial_American(S0, K, T, r, q, sigma, layers, call_put)
        price1 = binomial_American(S0, K, T, r, q, (sigma + dsigma), layers, call_put)

    vega = (price1 - price0)/dsigma
    return vega

# Newton method
def iv_newton(marketPrice, S0, K, T, r, q, call_put, type, model, layers, converCrit):
    x = 0.3
    if model == "BS":
        while abs(loss_function_bs(marketPrice, S0, K, T, r, q, x, call_put)) > converCrit:
            diff = vega_bs(S0, K, T, r, q, x)
            x = x - loss_function_bs(marketPrice, S0, K, T, r, q, x, call_put)/diff

        iv = x
        return iv
    else:
        while abs(loss_function_binomial(marketPrice, S0, K, T, r, q, x, call_put, layers, type)) > converCrit:
            diff = vega_binomial(S0, K, T, r, q, x, layers, call_put, type)
            x = x - loss_function_binomial(marketPrice, S0, K, T, r, q, x, call_put, layers, type)/diff

        iv = x
        return iv






# main
S0 = 50
K = 55
r = 0.1
q = 0.03
T = 0.5

# bisection method (checked)
print("==========BISECTION METHOD==========")
print("European Call")
print("--------------------")
marketPrice = 2.5
testBisec = iv_bisection(marketPrice, S0, K, T, r, q, call_put = "call", type = "European", model = "BS", layers = None, converCrit = 10**(-6))
print(f"IV of European Call : {round(testBisec*100, 4)} % (BS)")
testBisec = iv_bisection(marketPrice, S0, K, T, r, q, call_put = "call", type = "European", model = "CRR", layers = 100, converCrit = 10**(-6))
print(f"IV of European Call : {round(testBisec*100, 4)} % (CRR)")
print()

print("American Put")
print("--------------------")
marketPrice = 6.5
testBisec = iv_bisection(marketPrice, S0, K, T, r, q, call_put = "put", type = "American", model = "CRR", layers = 100, converCrit = 10**(-6))
print(f"IV of American Put : {round(testBisec*100, 4)} % (CRR)")
print("\n")

# Newton method (checked)
print("==========NEWTON METHOD==========")
print("European Call")
print("--------------------")
marketPrice = 2.5
testNewton = iv_newton(marketPrice, S0, K, T, r, q, "call", type = "European", model = "BS", layers = None, converCrit = 10**(-6))
print(f"IV of European Call : {round(testNewton*100, 4)} % (BS)")
testNewton = iv_newton(marketPrice, S0, K, T, r, q, "call", type = "European", model = "CRR", layers = 100, converCrit = 10**(-6))
print(f"IV of European Call : {round(testNewton*100, 4)} % (CRR)")
print()

print("American Put")
print("--------------------")
marketPrice = 6.5
testNewton = iv_newton(marketPrice, S0, K, T, r, q, "put", type = "American", model = "CRR", layers = 100, converCrit = 10**(-6))
print(f"IV of American Put : {round(testNewton*100, 4)} % (CRR)")
print("\n")
