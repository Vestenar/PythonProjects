def npp(a):
    k = 0
    n = len(a)
    d = [-1 for i in range(n)]
    for i in range(n):
        d[i] = 1
        for j in range(i):
            if a[i] % a[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    for i in range(n):
        k = max(k, d[i])
    print(k)
    print(d)
    return


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    npp(nums)


if __name__ == "__main__":
    main()


'''

15    
7 2 1 3 8 4 9 1 2 6 5 9 3 8 1

18
1  4  4  6  7  9 12 14 14 15 17 20 22 24 24 27 30 30
    
'''