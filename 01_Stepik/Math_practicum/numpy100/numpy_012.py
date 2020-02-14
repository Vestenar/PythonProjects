import numpy
numpy.random.seed(42)
n, m, l = [int(i) for i in input().split()]

Z = numpy.random.random_sample((n,m,l))
