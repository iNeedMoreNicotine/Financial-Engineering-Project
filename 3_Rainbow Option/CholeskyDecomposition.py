import scipy.linalg
import numpy as np

def cholesky_decomposition(cov_matrix):
    A = []
    n = len(cov_matrix)
    for i in range(n):
        A.append([0]*n)

    # step1
    A[0][0] = cov_matrix[0][0]**0.5
    for j in range(1,n):
        A[0][j] = cov_matrix[0][j]/A[0][0]

    # step2&3
    if n > 2:
        for i in range(1, n-1):
            temp = []
            for k in range(i):
                temp.append(A[k][i]**2)
            A[i][i] = (cov_matrix[i][i]-sum(temp))**0.5

            for j in range(i+1,n):
                temp = []
                for k in range(i):
                    temp.append(A[k][i]*A[k][j])
                A[i][j] = (cov_matrix[i][j]-sum(temp))/A[i][i]

    # step4
    temp = []
    for k in range(n-1):
        temp.append((A[k][n-1])**2)
    A[n-1][n-1] = (cov_matrix[n-1][n-1] - sum(temp))**0.5

    return A




# c = [[4,12,-16],[12,37,-43],[-16,-43,98]]
# print(cholesky_decomposition(c))
# print(scipy.linalg.cholesky(c))

T = 0.5
sigma1, sigma2, sigma3, sigma4, sigma5 = 0.5, 0.5, 0.5, 0.5, 0.5
c = [[sigma1**2*T, 0.5*sigma1*sigma2*T, 0.5*sigma1*sigma3*T, 0.5*sigma1*sigma4*T, 0.5*sigma1*sigma5*T],
     [0.5*sigma2*sigma1*T, sigma2**2*T, 0.5*sigma2*sigma3*T, 0.5*sigma2*sigma4*T, 0.5*sigma2*sigma5*T],
     [0.5*sigma3*sigma1*T, 0.5*sigma3*sigma2*T, sigma3**2*T, 0.5*sigma3*sigma4*T, 0.5*sigma3*sigma5*T],
     [0.5*sigma4*sigma1*T, 0.5*sigma4*sigma2*T, 0.5*sigma4*sigma3*T, sigma4**2*T, 0.5*sigma4*sigma5*T],
     [0.5*sigma5*sigma1*T, 0.5*sigma5*sigma2*T, 0.5*sigma5*sigma3*T, 0.5*sigma5*sigma4*T, sigma5**2*T]]
print('========================================================================================')
# print(cholesky_decomposition(c))
for row in cholesky_decomposition(c):
    print(row)
# print(np.transpose(cholesky_decomposition(c)).dot(cholesky_decomposition(c)))

print('========================================================================================')
print(scipy.linalg.cholesky(c))
# print(np.transpose(scipy.linalg.cholesky(c)).dot(scipy.linalg.cholesky(c)))

# c = [[3, 4, 3],
#      [4, 8, 6],
#      [3, 6, 9]]
# print(cholesky_decomposition(c))
# print(scipy.linalg.cholesky(c))