import math

def f(x):
  return x*x - 2*math.sin(x) + 0.7

def F1(x):
  return 2*x - 2*math.cos(x)

def F2(x):
  return 2 + 2*math.sin(x)

def fi(x):
  b = 3
  lam = 1 / f(b)
  return x - lam * f(x)   

a = 0.8
b = 3

eps = 0.000001

x0 = 1

x = fi(x0)

while(abs(x - x0) > eps):
  x0 = x
  x = fi(x0)

print(f(x))