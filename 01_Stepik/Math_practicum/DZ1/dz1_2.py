from math import exp

def f(x):
    return exp(x)

def def_e(x):
    dx = 0.00000001
    return round((f(x + dx) - f(x)) / dx, 3)

for i in range(0, 20, 2):
    print(round(f(i), 3), def_e(i))

