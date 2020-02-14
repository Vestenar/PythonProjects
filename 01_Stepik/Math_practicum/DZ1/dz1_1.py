def f(x):
    from math import atan
    return 2 * atan(x)

lim = f(float('inf'))
print(round(lim, 3))
