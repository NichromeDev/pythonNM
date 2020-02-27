import sympy as sp
import math

def w(i):
  ww = 1
  for g in range(n):
    if g != i:
        ww *= (x - X[g])
  return ww

def f(x):
  return 2*math.sin(x)

NN = 7

X = [math.pi/6, math.pi/4, math.pi/3, math.pi/2]

n = len(X)

x = sp.symbols('x', Float = True)

L = 0

for i in range(len(X)):
  L += (f(X[i]) * w(i)) / ((w(i).subs(x, X[i])))

print(sp.simplify(L))
