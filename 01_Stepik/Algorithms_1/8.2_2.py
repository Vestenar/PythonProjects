import cProfile
from random import randint
'''

решение за О(n**2)

'''

def npp(a):
    k = 0
    n = len(a)
    d = [1 for i in range(n)]
    for i in range(n):
        # print("i:", i, a[i])
        for j in range(i):
            # print("j", j, a[j])
            if a[i] <= a[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
            # print(d)
    k = max(d)
    print(k)
    # print(d)
    define(k,d)
    return


def define(k, d):
    ans = []
    l = len(d)
    for i in range(l - 1, -1, -1):
        if d[i] == k:
            ans.append(i + 1)
            k -= 1
    print(*(reversed(ans)))

    return


def main():
    # n = int(input())
    # nums = list(map(int, input().split()))
    n = 10**4
    nums = [randint(0, 10**5) for _ in range(n)]
    npp(nums)


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