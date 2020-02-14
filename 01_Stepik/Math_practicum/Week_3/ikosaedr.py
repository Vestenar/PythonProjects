from math import sqrt, ceil, tan, pi

def S(x):
    s6 = 3 * sqrt(3) * x**2 / 2

    s5 = 5 * x**2 / (4 * tan(2 * pi / 10))

    return 20 * s6 + 12 * s5

def S_ceil(x):
    return ceil(S(x))

print(S(5))
print(S_ceil(5))