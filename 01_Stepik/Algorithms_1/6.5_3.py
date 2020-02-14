from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
# a, b = map(sorted, zip(*(map(int, input().split()) for _ in range(n))))
a = []
b = []
for i in range(n):
    l, r = map(int, input().split())
    a.append(l)
    b.append(r)
a.sort()
b.sort()
# print(a, "\n", b)
dots = list(map(int, input().split()))
# print(p)
for p in dots:
    print(bisect_right(a, p) - bisect_left(b, p), end=" ")
# print(*(bisect_right(a, p) - bisect_left(b, p) for p in dots))



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
'''