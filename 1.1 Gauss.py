import numpy as np

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
print()

n = 5

# Прямой ход:
for k in range(0, n - 1):
  for i in range(k + 1, n):
    for j in range(n-1, k-1, -1):
      A[i][j] -= A[i][k] / A[k][k] * A[k][j]
      B[i] -= A[i][k] / A[k][k] * B[k]

x = np.zeros(n)

print(A)
print()
print(B)
print()
print()

# Обратный ход
for k in range(n - 1 , 0, -1):
  x[k] = (B[k] - sum((A[k][j]*x[j]) for j in range(k + 1, n))) / A[k][k]

print(A)
print()
print(B)
print()
print()

A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0], [0.5 * j, j, 0.3 * j, 0, 0.1 * l], [0, 0.3 * j, 10, -0.3 * j, 0.5 * l], [0.2*k, 0, -0.3*j, j, -0.1*j], [0, 0.1*k, 0.5*k, -0.1*j, j*m]])

print(x)
print()
print(np.dot(A, x))