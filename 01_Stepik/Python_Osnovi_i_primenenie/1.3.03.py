#Fibonaccii

def fib(x):
    if x ==1 or x ==0:
        return 1
    else:
        return fib(x-1)+fib(x-2)

y = fib(8)
print(y)