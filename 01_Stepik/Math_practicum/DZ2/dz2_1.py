def f(x):
    return (2 * x**2 - 3 * x - 5) / (3 * x**2 + x + 1)

for i in (float(10**10), float(-10**10)):
    print(round(f(i), 3))
