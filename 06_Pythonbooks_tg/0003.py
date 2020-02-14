def fibonacci(length):
    fib1, fib2 = 1, 1
    num = 2

    while length > len(str(fib2)):
        fib1, fib2 = fib2, fib1 + fib2
        num += 1
    return num

def main():
    length = 1000
    print(fibonacci(length))


if __name__ == '__main__':
    main()
