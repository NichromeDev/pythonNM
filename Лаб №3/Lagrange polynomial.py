import sympy as sp

def w(i):
  ww = 1
  for g in range(n):
    if g != i:
        ww *= (x - X[g])
  return ww

NN = 7

X = [-2, -1, 0, 1, 2]
Y = [-7, -1, 9, 11, 17]

n = len(X)

x = sp.symbols('x', Float = True)

L = 0

for i in range(len(X)):
  L += (Y[i] * w(i)) / ((w(i).subs(x, X[i])))

print(sp.simplify(L))