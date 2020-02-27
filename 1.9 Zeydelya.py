import numpy as np

N = int(input("Введите номер варианта: "))

j = 1.5 + 0.1 * N
m = 1
k = j
l = k - 0.1

A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0], [0.5 * j, j, 0.3 * j, 0, 0.1 * l], [0, 0.3 * j, 10, -0.3 * j, 0.5 * l], [0.2*k, 0, -0.3*j, j, -0.1*j], [0, 0.1*k, 0.5*k, -0.1*j, j*m]])

b = np.array([-j + 0.05 * j*j, -0.8 * j + 0.1 * j*j - 0.02 * l * j, -10 + 0.03 * j*j - 0.1 * l * j, -0.2 * k + 0.3 * j + 0.02 * j*j, 0.01 * k * j - 0.5 * k - 0.2 *j*j])

print(A)
print()
print(b)
print()

n = 5

L = np.zeros((n,n))
D = np.zeros((n,n))
R = np.zeros((n,n))

for i in range(n):
  for j in range(n):
    if i > j:
      L[i,j] = A[i,j]
    if i == j:
      D[i,j] = A[i,j]
    if i < j:
      R[i,j] = A[i,j]


print(L, "\n")
print(D, "\n")
print(R, "\n")

B = np.dot(-np.linalg.inv(L + D), R)
c = np.dot(np.linalg.inv(L + D),b)

x = [1,0,0,0,0]
x1 = np.dot(B, x) + c

eps = 0.000001

while(True):
  if np.linalg.norm(x1 - x) < eps:
    break
  x = x1
  x1 = np.dot(B, x) + c
  

print(x1, "\n")
print(np.linalg.solve(A,b))
