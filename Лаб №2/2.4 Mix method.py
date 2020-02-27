import math

def f(x):
  return x*x - 2*math.sin(x) + 0.7

def F(x):
  return 2*x - 2*math.cos(x)

def F2(x):
  return 2 + 2*math.sin(x)

a = 0.8
b = 3

eps = 0.000001

x1 = a
x2 = b

while(abs(f((x2+x1) / 2)) > eps):
  x1 = a
  x2 = b
  x1 -= (f(x1) / (f(b) - f(x1))) * (b - x1)
  x2 -= f(x2)/F(x2)
  a = x1
  b = x2

print(f((a+b) / 2))