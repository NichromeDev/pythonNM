import numpy as np

def Jordan(A):
  n = 5
  for k in range(0, n - 1):
    for i in range(k + 1, n):
      for j in range(n-1, k-1, -1):
        A[i][j] -= A[i][k] / A[k][k] * A[k][j]

  result = 1
  for i in range(n):
    result *= A[i, i]
  return result

def LU(A):
  L = np.eye(n)
  U = np.zeros((n,n))
  for i in range(n):
      for j in range(n):
          if (i <= j):
              U[i, j] = A[i, j] - sum((L[i, k] * U[k, j]) for k in range(i))
          if (i > j):
              L[i, j] = (A[i, j] - sum((L[i][k]*U[k][j]) for k in range(j))) / U[j, j]
  resultL = 1
  resultU = 1
  for i in range(n):
    resultL *= L[i, i]
    resultU *= U[i, i] 
  return resultL*resultU

N = int(input("Введите номер варианта: "))

j = 1.5 + 0.1 * N
m = 1
k = j
l = k - 0.1

A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0], [0.5 * j, j, 0.3 * j, 0, 0.1 * l], [0, 0.3 * j, 10, -0.3 * j, 0.5 * l], [0.2*k, 0, -0.3*j, j, -0.1*j], [0, 0.1*k, 0.5*k, -0.1*j, j*m]])

B = np.array([-j + 0.05 * j*j, -0.8 * j + 0.1 * j*j - 0.02 * l * j, -10 + 0.03 * j*j - 0.1 * l * j, -0.2 * k + 0.3 * j + 0.02 * j*j, 0.01 * k * j - 0.5 * k - 0.2 *j*j])

print(A)

print()

n = 5

np.linalg.det(A)


print(np.linalg.det(A), '\n')
print(Jordan(A), '\n')
print(LU(A), '\n')