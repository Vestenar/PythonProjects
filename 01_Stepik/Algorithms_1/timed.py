import time
from functools import lru_cache


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


cache = {}


def fib(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib(n - 2) + fib(n - 1)
    return cache[n]


fib1 = lru_cache(maxsize=None)(fib)  # декорирование с помощью стандартной библиотеки

if __name__ == "__main__":

    print(fib1(800))
    print("Время работы функции {:.7} секунд".format(timed(fib1, 1500)))