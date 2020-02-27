import numpy as np

N = int(input("Введите номер варианта: "))

j = 1.5 + 0.1 * N
m = 1
k = 0
l = 0

A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0], [0.5 * j, j, 0.3 * j, 0, 0.1 * l], [0, 0.3 * j, 10, -0.3 * j, 0.5 * l], [0.2*k, 0, -0.3*j, j, -0.1*j], [0, 0.1*k, 0.5*k, -0.1*j, j*m]])

r = np.array([-j + 0.05 * j*j, -0.8 * j + 0.1 * j*j - 0.02 * l * j, -10 + 0.03 * j*j - 0.1 * l * j, -0.2 * k + 0.3 * j + 0.02 * j*j, 0.01 * k * j - 0.5 * k - 0.2 *j*j])

print(A)
print()
print(r)
print()

n = 5

d = []
c = []
b = []
b.append(0)

for i in range(n):
  for j in range(n):
    if i == j:
      c.append(A[i, j])
    if i > j and A[i, j] != 0:
      d.append(A[i, j])
    if i < j and A[i, j] != 0:
      b.append(A[i, j])
d.append(0)



gm = np.zeros(n)
lm = np.zeros(n)

gm[0] = - d[0]/c[0]
lm[0] = r[0]/c[0]

for i in range(1,n):
  gm[i] = -(d[i]/(c[i] + b[i]*gm[i-1]))
  lm[i] = (r[i] - b[i]*lm[i - 1])/(c[i] + b[i]*gm[i-1])

x = np.zeros(n)

x[n-1] = (r[n-1] - b[n-1]*lm[n-2]) / (c[n-1] + b[n-1]*gm[n-2])

print(x[n-1], '\n')

for i in range(n - 2, -1, -1):
  x[i] = gm[i]*x[i+1] + lm[i]

print(x, '\n')

print(np.linalg.solve(A,r))