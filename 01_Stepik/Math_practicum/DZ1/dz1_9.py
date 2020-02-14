def fib(n):
    f0 = 1
    f1 = 1
    for i in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


for i in range(5):
    print(fib(i))