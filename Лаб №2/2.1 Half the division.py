import math

def f(x):
  return x*x - 2*math.sin(x) + 0.7

a = 0.8
b = 3

eps = 0.00000000000001

while(abs(f((a+b)/2)) > eps):
  c = (b + a) / 2
  if f(a) * f(c) < 0:
    b = c
  if f(c) * f(b) < 0:
    a = c

print(f((a+b)/2))
