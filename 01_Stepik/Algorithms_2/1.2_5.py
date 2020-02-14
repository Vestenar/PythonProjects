def push(s, x):
    s.append((x, max(x, s[-1][1]) if s else x))


n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
s1, s2 = [], []

for x in A[:m]:
    push(s1, x)
print(s1[-1][1], end=" ")

for x in A[m:]:
    if not s2:
        while s1:
            push(s2, s1.pop()[0])

    s2.pop()
    push(s1, x)
    print(s1, s2)
    if not s1:
        print(s2[-1][1], end=" ")
    elif not s2:
        print(s1[-1][1], end=" ")
    else:
        print(max(s1[-1][1], s2[-1][1]), end=" ")
