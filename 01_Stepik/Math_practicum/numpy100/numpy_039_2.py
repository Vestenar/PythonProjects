import numpy

start, stop, n = [int(input()) for _ in range(3)]

Z = numpy.around(numpy.geomspace(start, stop, num=n), 3)

print(Z)