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

c = np.column_stack((A, B))

print(c, "\n")

#Прямой ход
for i in range(n):
    main_elem = c[i,i]
    for j in range(n + 1):
        c[i,j] = c[i,j] / main_elem    
    for k in range(i + 1, n):
        first_elem = c[k, i]
        for l in range(n + 1):
            c[k, l] -= c[i, l] * first_elem
print(c, "\n")

#Обратный ход
for i in range(n - 1, -1, -1):
    for k in range(i - 1, -1, -1):
        last_elem = c[k,i]
        for j in range(n, -1, -1):
            c[k,j] -= c[i,j] * last_elem
print(c, "\n")

print(np.linalg.solve(A, B))
