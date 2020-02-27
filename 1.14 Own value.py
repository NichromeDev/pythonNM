import numpy as np

N = int(input("Введите номер варианта: "))

j = 1.5 + 0.1 * N
m = 1
k = N
l = N

A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0], [0.5 * j, j, 0.3 * j, 0, 0.1 * l], [0, 0.3 * j, 10, -0.3 * j, 0.5 * l], [0.2*k, 0, -0.3*j, j, -0.1*j], [0, 0.1*k, 0.5*k, -0.1*j, j*m]])

print(A)
print()

C = A

n = 5

#

y = [1,1,1,1,1]
Y = np.dot(A, y)

lam_1 = Y[0]/y[0]

y = Y
Y = np.dot(A, y)
lam_2 = Y[0]/y[0]

eps = 0.00001

while(abs(lam_1 - lam_2) > eps):
  lam_1 = lam_2
  y = Y
  Y = np.dot(A, y)
  lam_2 = Y[0]/y[0]

lam  = lam_2

print(lam, '\n')
print(Y / np.linalg.norm(Y), '\n')

# Минимальный по модулю

A = np.linalg.inv(A)

y = [1,1,1,1,1]
Y = np.dot(A, y)

lam_1 = Y[0]/y[0]

y = Y
Y = np.dot(A, y)
lam_2 = Y[0]/y[0]

eps = 0.001

while(abs(lam_1 - lam_2) > eps):
  lam_1 = lam_2
  y = Y
  Y = np.dot(A, y)
  lam_2 = Y[0]/y[0]

print(1/lam_2, '\n')
print(Y / np.linalg.norm(Y), '\n')
print(np.linalg.eig(C))