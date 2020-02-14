def filling(W, iters):
    total = 0
    while W and iters:
        if W >= iters[-1][1]:
            total += iters[-1][0]
            W -= iters[-1][1]
        else:
            total += W * iters[-1][0] / iters[-1][1]
            W = 0
        iters.pop()
    print('{:.3f}'.format(total))
    return


def main():
    staff = []
    n, W = map(int, input().split())
    for _ in range(n):
        cost, wol = map(int, input().split())
        staff.append([cost, wol])
    staff.sort(key=lambda x: x[0]/x[1])
    filling(W, staff)

if __name__ == "__main__":
    main()

'''

3 100
1000 99
2000 3
66 5

'''