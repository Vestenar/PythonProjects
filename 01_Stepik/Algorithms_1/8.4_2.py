def calc(n):
    D = [0] + [float("inf") for _ in range(n-1)]
    prev = [0 for _ in range(n)]
    ans = []
    for i in range(1, n + 1):
        for k in (i * 3, i * 2, i + 1):
            if k <= n:
                if D[k - 1] > D[i - 1] + 1:
                    D[k - 1] = D[i - 1] + 1
                    prev[k - 1] = i

    while n >= 1:
        ans.insert(0, n)
        n = prev[n-1]
    print(D[-1])
    print(*ans)
    return


def main():
    k = int(input())
    calc(k)


if __name__ == "__main__":
    main()
