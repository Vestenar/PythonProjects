def is_prime(n):
    from math import sqrt
    for i in range(2, 1 + int(sqrt(n))):
        if n % i == 0: return False
    return True

for i in range(10):
    print(f'{i=} : {is_prime(i)}')

print(is_prime(7))