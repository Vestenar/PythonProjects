from random import shuffle, seed
seed(42)

def disc_generator(alphabet):
    alphabet = list(alphabet)
    shuffle(alphabet)
    alphabet = "".join(alphabet)
    return alphabet



alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(6):
    a = disc_generator(alphabet)
    print(a)
