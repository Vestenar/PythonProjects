def covering(otr):
    count = 0
    dots = []
    while otr:
        sample = otr[0]
        dots.append(sample[-1])
        count += 1
        otr = list(filter(lambda x: x[0] > dots[-1], otr))
    print(count)
    for dot in dots:
        print(dot, end=" ")
    return


def main():
    otr = []
    n = int(input())
    for _ in range(n):
        l, r = map(int,(input().split()))
        otr.append([l, r])
    otr.sort(key=lambda x: x[-1])
    covering(otr)


if __name__ == "__main__":
    main()
