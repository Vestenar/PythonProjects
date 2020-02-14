def constructShell(n):
    return [[0]*j for j in list(range(1, n+1))+list(range(n-1, 0, -1))]


print(constructShell(1))