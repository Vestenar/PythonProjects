def f(x):                   # функция, для которой ищем производную
    return x ** 2

def g(x):                   # функция, описывающая касательную
    return a * x + b


x0 = 2
dx_list = [0.1, 0.01, 0.001, 0.0001]

for dx in dx_list:          # по определению производной
    print((f(x0 + dx) - f(x0)) / dx)

x0 = 1
dx = 0.00001

a = (f(x0 + dx) - f(x0)) / dx       # из геометрического смысла производной
b = f(x0) - a * x0                  # из уравнения общей точки графиков

print(a, b)

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-1, 2, 0.01)
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.grid()
plt.show()