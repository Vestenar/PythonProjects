import time
from functools import lru_cache
start_time = time.time()
# @lru_cache()
def super_L(n):
    if n == 1: return 1
    if n == 0: return 2
    if n % 6 == 0: return L6(n // 6)
    if n % 5 == 0: return L5(n // 5)
    if n % 4 == 0: return L4(n // 4)
    if n % 3 == 0: return L3(n // 3)
    if n % 2 == 0: return L2(n // 2)
    return super_L(n - 2) + super_L(n - 1)

def L2(n):
    return super_L(n)**2 - 2 * (-1)**n

def L3(n):
    return super_L(n)**3 - 3 * (-1)**n * super_L(n)

def L4(n):
    return super_L(n)**4 - 4 * (-1)**n * super_L(n)**2 + 2

def L5(n):
    return super_L(n)**5 - 5 * (-1)**n * super_L(n)**3 + 5 * super_L(n)

def L6(n):
    return super_L(n)**6 - 6 * (-1)**n * super_L(n)**4 + 9 * super_L(n)**2 - 2 * (-1)**n

print(super_L(2**26))

print(f"--- {time.time() - start_time} seconds---")