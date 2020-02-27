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

c = np.column_stack((A, -B))

y = np.zeros(n + 1)
y[n] = 1
c = np.row_stack((c, y))

print(c)

u = np.zeros((n+1, n+1))
v = np.zeros((n+1, n+1))
u[0] = c[0]
v[0] = u[0] / np.linalg.norm(u[0])

for j in range(1, n+1):
  u[j] = c[j] - sum(np.dot(c[j],v[i])*v[i] for i in range(j))
  v[j] = u[j] / np.linalg.norm(u[j])

print(u[5,:5]/u[5,5])