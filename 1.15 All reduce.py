import numpy as np



def LU(A):
  n = 5

  L = np.eye(n)

  U = np.zeros((n,n))

  for i in range(n):
      for j in range(n):
          if (i <= j):
              U[i, j] = A[i, j] - sum((L[i, k] * U[k, j]) for k in range(i))
          if (i > j):
              L[i, j] = (A[i, j] - sum((L[i][k]*U[k][j]) for k in range(j))) / U[j, j]
  return(L, U)

N = int(input("Введите номер варианта: "))

j = 1.5 + 0.1 * N
m = 1
k = N
l = N

A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0], [0.5 * j, j, 0.3 * j, 0, 0.1 * l], [0, 0.3 * j, 10, -0.3 * j, 0.5 * l], [0.2*k, 0, -0.3*j, j, -0.1*j], [0, 0.1*k, 0.5*k, -0.1*j, j*m]])

print(A)
print()

n = 5

A0 = A
L, U = LU(A)
A1 = np.dot(U, L)

eps = 0.01

while(np.linalg.norm(A1-A0, 2) > eps):
  A0 = A1
  L, U = LU(A0)
  A1 = np.dot(U, L)

print(np.diagonal(A1))

print(np.linalg.eig(A))