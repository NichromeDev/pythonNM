import numpy as np

N = int(input("Введите номер варианта: "))

j = 1.5 + 0.1 * N
m = 1
k = N
l = N

A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0], [0.5 * j, j, 0.3 * j, 0, 0.1 * l], [0, 0.3 * j, 10, -0.3 * j, 0.5 * l], [0.2*k, 0, -0.3*j, j, -0.1*j], [0, 0.1*k, 0.5*k, -0.1*j, j*m]])

B = np.array([-j + 0.05 * j*j, -0.8 * j + 0.1 * j*j - 0.02 * l * j, -10 + 0.03 * j*j - 0.1 * l * j, -0.2 * k + 0.3 * j + 0.02 * j*j, 0.01 * k * j - 0.5 * k - 0.2 *j*j])

print(A)
print()
print(B)
print()

n = 5

D = np.eye(n)
S = np.zeros((n, n))

print(D, '\n')

for i in range(n):
  D[i, i] = np.sign(A[i, i] - sum((S[p, i] * S[p, i] * D[p, p]) for p in range(i)))
  S[i, i] = np.sqrt(abs(A[i, i] - sum((S[p, i] * S[p, i] * D[p, p]) for p in range(i))))
  for j in range(i + 1, n):
    S[i, j] = (A[i,j] - sum((S[p,i]*D[p,p]*S[p,j])for p in range(i))) / (D[i,i] * S[i,i])

St = np.transpose(S)

y = np.zeros(n)
x = np.zeros(n)
StD = np.dot(St, D)

for k in range(n):
    y[k] = (B[k] - sum((StD[k,j] * y[j]) for j in range(k))) / StD[k,k]

for k in range(n - 1, -1, -1):
    x[k] = (y[k] - sum((S[k, j] * x[j]) for j in range(k, n))) / S[k, k]

print(y, '\n')
print(x)

