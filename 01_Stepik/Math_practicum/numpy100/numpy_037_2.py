import numpy as np

n, m = map(int, input().split())
k = int(input())

Z = np.zeros((n,m)).transpose()
M = np.arange(k, n+k)
Z += M
Z = Z.transpose()
print(Z)
print(M)