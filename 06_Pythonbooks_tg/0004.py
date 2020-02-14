from math import pow


def finder(n):
    a = []
    for p in range(2, 10):
        for base in range(2, 100):
            num = int(pow(base, p))
            if base == sum(list(map(int, str(num)))):
                a.append((num, base, p))

    a = sorted(a)
    for id, (i, j, k) in enumerate(a):
        print(id + 1, i, '{} ** {}'.format(j, k))

    print('30й член последовательности: {}\nэто {} = {} в степени {}'.format(a[n-1][0], '+'.join(str(a[n-1][0])), a[n-1][1], a[n-1][2]))
    return a


def main():
    n = 30
    finder(n)


if __name__ == '__main__':
    main()
