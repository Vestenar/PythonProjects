import numpy as np

kk, n = map(int, input().split())

Z = np.diag(np.arange((n)) + 1, k=kk)

print(Z)
