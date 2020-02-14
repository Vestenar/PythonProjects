import numpy
import random

numpy.random.seed(int(input()))
Z = numpy.random.random_sample(int(input()))
Z.sort()
print(Z)