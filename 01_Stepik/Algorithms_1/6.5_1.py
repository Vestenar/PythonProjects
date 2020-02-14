from random import randint
from bisect import bisect_right

os = []
osr = []

def quicksort(a, l, r):
    while l < r:
        m = m_partition(a, l, r)
        quicksort(a, l, m - 1)
        l = m + 1


def m_partition(a, l, r):
    if r - l >= 3:
        m = []
        for i in range(3):
            m.append(randint(l, r))
        m.sort()
        i = m[1]
        a[r], a[i] = a[i], a[r]
        return partition(a, l, r)
    else:
        i = randint(l, r)
        a[r], a[i] = a[i], a[r]
    return partition(a, l, r)


def partition(a, l, r):
    x = a[l]
    i = l
    j = i
    for i in range((l + 1), (r + 1)):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def count(dot):
    os_id = 0
    count = 0
    while os_id < len(os):
        if os[os_id][0] <= dot:
            if os[os_id][1] >= dot:
                count += 1
            else:
                os_id += 1
                continue
        else:
            break
        os_id += 1
    return count


def count2(dot):
    count = 0

    i = bisect_right(osr, dot)
    for o in os[:i]:
        if o[0] <= dot <= o[1]:
            count += 1
    return count

def main():
    n, m = map(int, input().split())
    global os, osr
    for _ in range(n):
        l, r = map(int, input().split())
        os.append((l, r))
    dots = list(map(int, input().split()))
    print(os)
    quicksort(os, 0, len(os) - 1)
    osr = [o[0] for o in os]
    print(os)
    print(osr)
    result = []
    for dot in dots:
        result.append(count2(dot))

    print(" ".join(str(x) for x in result))


if __name__ == "__main__":
    main()

'''
10 5
-2 3
0 3
-1 0
-1 3
0 1
-2 -1
1 3
2 3
1 2
2 3
-3 -1 0 2 3

ans = 0 4 5 7 6
'''