def count(n):
    sum = []
    s = 1
    while n - s > s:
        n -= s
        sum.append(s)
        s += 1
    else: sum.append(n)

    print(len(sum))
    for s in sum:
        print(s, end=" ")
    return


def main():
    n = int(input())
    count(n)


if __name__ == "__main__":
    main()
