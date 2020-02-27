import math

def f(x):
  return x*x - 2*math.sin(x) + 0.7

def F(x):
  return 2*x -2*math.cos(x)

a = 0.8
b = 3

eps = 0.000001

x = (a+b)/2

while (abs(f(x)) > eps):
  x -= f(x)/F(x)

print((f(x)))