def knapsack(W, w):
    D = [[0 for _ in range(W + 1)] for _ in range(len(w))]
    for i in range(1, len(w)):
        for j in range(1, W + 1):
            D[i][j] = D[i - 1][j]
            if w[i] <= j:
                D[i][j] = max(D[i - 1][j], D[i - 1][j - w[i]] + w[i])

    for d in D:
        print(d)
    return D[-1][-1]


def main():
    W, n = map(int, input().split())
    w = [0] + [int(i) for i in input().split()]
    print(knapsack(W, w))


if __name__ == "__main__":
    main()
