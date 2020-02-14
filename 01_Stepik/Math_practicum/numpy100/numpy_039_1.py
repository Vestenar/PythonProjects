import numpy

start, stop, n = [int(input()) for _ in range(3)]

Z = numpy.linspace(start, stop, num=n + 1, endpoint=False)[1:]
Z = numpy.around(Z, 4)
print(Z)