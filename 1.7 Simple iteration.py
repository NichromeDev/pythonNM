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
lam = 1/2

S = np.linalg.inv(A)*lam
E = np.eye(n)
B = E - np.dot(S, A)
c = np.dot(S,b)

print(c)

x = [1,0,0,0,0]
x1 = np.dot(B, x) + c

eps = 0.000001

while(True):
  print(x, "\n")
  print(x1, "\n")
  if np.linalg.norm(x1 - x) < eps:
    break
  x = x1
  x1 = np.dot(B, x) + c
  

#print(x1, "\n")
print(np.linalg.solve(A,b))
