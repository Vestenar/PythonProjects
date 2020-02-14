def mkdistmtrx(a, b):
    n = len(a)
    m = len(b)
    d = [[j] + [i if j == 0 else 0 for i in range(1, n+1)] for j in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            w = [d[i - 1][j], d[i][j - 1], b[i - 1], a[j - 1]]  # отладочная информация
            s1 = d[i - 1][j] + 1
            s2 = d[i][j - 1] + 1
            c = b[i - 1] != a[j - 1]
            s3 = d[i - 1][j - 1] + c
            d[i][j] = min(s1, s2, s3)

    print(d[-1][-1])

    print("     ", "  ".join(i for i in a), sep=" ")
    for line in zip(" "+b, d):
        print(*line)


def main():
    a, b = input().strip(), input().strip()
    # a = "editing"
    # b = "distance"
    if len(a) <= len(b):
        mkdistmtrx(a, b)
    else:
        mkdistmtrx(b, a)

if __name__ == "__main__":
    main()
