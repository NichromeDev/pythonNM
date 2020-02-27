import numpy as np

def func(A, B):
  n = 6
  c = np.column_stack((A, -B))

  y = np.zeros(n + 1)
  y[n] = 1
  c = np.row_stack((c, y))

  u = np.zeros((n+1, n+1))
  v = np.zeros((n+1, n+1))
  u[0] = c[0]
  v[0] = u[0] / np.linalg.norm(u[0])

  for j in range(1, n+1):
    u[j] = c[j] - sum(np.dot(c[j],v[i])*v[i] for i in range(j))
    v[j] = u[j] / np.linalg.norm(u[j])

  return(u[n,:n]/u[n,n])

N = int(input("Введите номер варианта: "))

j = 1.5 + 0.1 * N
n = 3

A = np.array([[complex(1, -j), 0, complex(0,-j)], [complex(-j, -2), complex(0,-j), complex(2, j)], [complex(0, 1), 2, j]])

B = np.array([complex(1 + j, -3*j), complex(-3*j + 4, 2*j),complex(2*j, (j - 1))])

print(A)
print()
print(B)
print()

A1 = A.real
A2 = A.imag

B1 = B.real
B2 = B.imag

C = np.row_stack((np.column_stack((A1, -A2)), np.column_stack((A2, A1))))
print(C, '\n')

d = np.append(B1,B2)
print(d, '\n')

print(np.linalg.solve(C,d), '\n')
temp = func(C,d)

x = np.zeros(n, 'complex')

for i in range(n):
  x[i]=complex(temp[i], temp[i + 3])

print(x)