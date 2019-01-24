import itertools

def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def is_prime(num):
    if num == 2: return True
    if num % 2 == 0: return False
    for _ in range(3, num // 2, 2):
        if num % _ == 0:
            return False
    return True
print(list(itertools.takewhile(lambda x : x <= 31, primes())))