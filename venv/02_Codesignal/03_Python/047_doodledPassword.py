from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    print(res)
    deque(map(lambda x: res[x].rotate(-x), range(n)), 0)
    print(deque(map(lambda x: res[x].rotate(-x), range(n)), 0))
    print(res)
    return [list(d) for d in res]


dig = [1, 2, 3, 4, 5]
print(doodledPassword(dig))