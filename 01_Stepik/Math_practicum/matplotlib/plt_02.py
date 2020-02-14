import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 5., 0.01)

def f(x):
    return x**2

def g(x):
    return 1 / x

def h(x):
    return x * np.sin(x)


fig, axes = plt.subplots(figsize=(13, 8), dpi=120)
axes.plot(x, f(x), x, g(x))
axes.plot(x, h(x))
axes.legend(['f(x)', 'g(x)', 'h(x)'])
# fig.show()

fig, axes = plt.subplots(figsize=(13, 8), dpi=120)
axes.plot(x, f(x), label='$x^2$')               # latex разметка
axes.plot(x, g(x), label=r'$\frac{1}{x}$')
axes.plot(x, h(x), label=r'$x \cdot sin(x)$')
axes.legend(loc=5, fontsize=16)
axes.set_xlabel('Абсцисса')
axes.set_ylabel('Ордината')
axes.set_title('Заголовок', fontsize=16)
fig.show()
