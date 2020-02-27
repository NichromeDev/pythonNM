import numpy as np
import scipy as sc
from scipy.linalg import lu

N = int(input("Введите номер варианта: "))

j = 1.5 + 0.1 * N
m = 1
k = j
l = k - 0.1

A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0], [0.5 * j, j, 0.3 * j, 0, 0.1 * l], [0, 0.3 * j, 10, -0.3 * j, 0.5 * l], [0.2*k, 0, -0.3*j, j, -0.1*j], [0, 0.1*k, 0.5*k, -0.1*j, j*m]])

B = np.array([-j + 0.05 * j*j, -0.8 * j + 0.1 * j*j - 0.02 * l * j, -10 + 0.03 * j*j - 0.1 * l * j, -0.2 * k + 0.3 * j + 0.02 * j*j, 0.01 * k * j - 0.5 * k - 0.2 *j*j])

print(A)
print()
print(B)
print()

n = 5

L = np.eye(n)

#print(L, '\n')

U = np.zeros((n,n))

#print(U, '\n')

for i in range(n):
    for j in range(n):
        if (i <= j):
            U[i, j] = A[i, j] - sum((L[i, k] * U[k, j]) for k in range(i))
        if (i > j):
            L[i, j] = (A[i, j] - sum((L[i][k]*U[k][j]) for k in range(j))) / U[j, j]

print(U, '\n')
print(L, '\n')

#print(np.dot(L, U), '\n')

y = np.zeros(n)

for k in range(n):
    y[k] = B[k] - sum((L[k, j]*y[j]) for j in range(k))

print(y, '\n')

x = np.zeros(n)

for k in range(n - 1, -1, -1):
    x[k] = (y[k] - sum((U[k, j]*x[j]) for j in range(k, n))) / U[k, k]

print(x, sep='\n')
print(np.linalg.solve(A, B))
