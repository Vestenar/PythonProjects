import matplotlib.pyplot as plt
import numpy as np

x = range(-10, 11)
y = [i**2 for i in x]

plt.figure()
plt.plot(x, y, 'm')
plt.xlabel('X axe')
plt.ylabel('Y axe')
plt.title('Title')
# plt.show()

fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1])           # оси для графика
axes.plot(x, y, 'r')
axes2 = fig.add_axes([0.3, 0.5, 0.4, 0.4])  # вторая ось со смещением
axes2.plot(y, x, 'g')
fig.show()

fig, axes = plt.subplots()
axes.plot(x, y, 'r')
# fig.show()

fig, axes = plt.subplots(2)
axes[0].plot(x, y, 'r')
axes[1].plot(y, x, 'g')
# fig.show()

fig, axes = plt.subplots(1, 2, figsize=(13,8))      # 1 строка , 2 столбца
axes[0].plot(x, y, 'r')                             # c размерами 13 x 8 inch
axes[1].plot(y, x, 'g')
# fig.show()

fig, axes = plt.subplots(2, 2, figsize=(13,8))      # 2 строки , 2 столбца
axes[0][0].plot(x, y, 'r')                          # обращение графиков как к матрице
axes[0][0].set_xlabel('X axes')
axes[0][0].set_ylabel('Y axes')
axes[0][0].set_title('Title')
axes[1][0].plot(y, x, 'g')
axes[1][0].set_xlabel('X axes')
axes[1][0].set_ylabel('Y axes')
axes[1][0].set_title('Title')
fig.tight_layout()                                  # устранение наползания заголовка на обозначение оси Х
# fig.show()

