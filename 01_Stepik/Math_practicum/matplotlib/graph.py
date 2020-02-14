import matplotlib.pyplot as plt
import numpy
c = [1., 0., 0., -1., 0., 1.]

def f(x, c):
    return c[0]+c[1]*x+c[2]*x**2+c[3]*x**3+c[4]*x**4 + c[5]*x**5

x = numpy.arange(-20, 20, 0.01) #Массив значений аргумента

plt.plot(x, f(x, c)) #Построение графика
plt.xlim([0.75, 0.8])
plt.ylim([0.8, 0.84])
plt.xlabel(r'$x$') #Метка по оси x в формате TeX
plt.ylabel(r'$f(x)$') #Метка по оси y в формате TeX
plt.grid(True) #Сетка
plt.show() #Показать график
