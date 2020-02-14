import cProfile
from random import randint
from bisect import bisect_right


'''

решение за О(nlogn)

'''


def binary(a):
    d, prev = [], []
    for i, x in enumerate(a):
        j = bisect_right(d, [-x, i])
        if j == len(d):
            d.append([-x, i])
        else:
            if -d[j][0] < x:
                d[j] = [-x, i]

        prev.append(d[j - 1][1] if j else None)
        print(d)
        print(prev)


    out = [d[-1][1]]
    print(out)
    while prev[out[-1]] is not None:
        out.append(prev[out[-1]])
    print(out)
    print(len(out), ' '.join(str(x + 1) for x in reversed(out)), sep='\n')


def main():
    # _, a = input(), list(map(int, input().split()))

    n = 10**1 * 2
    a = [randint(0, 10**1//2) for _ in range(n)]
    print(a)

    binary(a)


if __name__ == "__main__":
    # main()
    cProfile.run("main()")
'''

15    
7 2 1 3 8 4 9 1 2 6 5 9 3 8 1

18
1  4  4  6  7  9 12 14 14 15 17 20 22 24 24 27 30 30

10
5 5 7 8 4 4 6 3 2 1

'''