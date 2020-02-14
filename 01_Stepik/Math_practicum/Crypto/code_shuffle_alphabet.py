def disc_generator(alphabet):
    from random import shuffle, seed
    alphabet = list(alphabet)

    for i in range(6):
        seed(42)
        shuffle(alphabet)
        print("".join(alphabet))
    return

print(disc_generator('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))