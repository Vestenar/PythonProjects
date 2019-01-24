from random import random

def random_generator(k):
    for i in range(k):
        yield random()

gen = random_generator(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
