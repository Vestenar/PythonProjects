import numpy as np

n, m = map(int, input().split())
k = int(input())

Z = np.zeros((n,m))
M = np.arange(k, m+k)
Z = Z + M
print(Z)
print(M)