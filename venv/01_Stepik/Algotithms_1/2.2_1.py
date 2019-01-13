def fib(n):
    fib = [1, 1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib[-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()


'''
Дано целое число 1≤n≤40, необходимо вычислить n-е число Фибоначчи
(напомним, что F0=0, F1=1 и Fn=Fn−1+Fn−2 при n≥2).
'''