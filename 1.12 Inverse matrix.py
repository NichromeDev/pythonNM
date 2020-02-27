import numpy as np

def func(A, B):
  n = 5

  L = np.eye(n)
  U = np.zeros((n,n))

  for i in range(n):
      for j in range(n):
          if (i <= j):
              U[i, j] = A[i, j] - sum((L[i, k] * U[k, j]) for k in range(i))
          if (i > j):
              L[i, j] = (A[i, j] - sum((L[i][k]*U[k][j]) for k in range(j))) / U[j, j]

  y = np.zeros(n)

  for k in range(n):
      y[k] = B[k] - sum((L[k, j]*y[j]) for j in range(k))

  x = np.zeros(n)

  for k in range(n - 1, -1, -1):
      x[k] = (y[k] - sum((U[k, j]*x[j]) for j in range(k, n))) / U[k, k]

  return(x)


N = int(input("Введите номер варианта: "))

j = 1.5 + 0.1 * N
m = 1
k = j
l = k - 0.1
n = 5

A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0], [0.5 * j, j, 0.3 * j, 0, 0.1 * l], [0, 0.3 * j, 10, -0.3 * j, 0.5 * l], [0.2*k, 0, -0.3*j, j, -0.1*j], [0, 0.1*k, 0.5*k, -0.1*j, j*m]])

E = np.eye(n)

print(A,'\n')

print(E,'\n')

x = []

for i in range(n):
  x.append(func(A,E[i]))

x = np.array(x)
x = x.transpose()

print(x, '\n')

print(np.dot(A, x))
