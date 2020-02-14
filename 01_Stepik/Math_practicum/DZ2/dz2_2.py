from math import sin, pi
def f(x):
    return (sin(pi * x / 2)) / x


for i in (10**12, -10**12):
    print(f(i))