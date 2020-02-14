import numpy as np

n, m = map(int, input().split())
Z = np.zeros((n,m))
for i in range(2):
    Z[0] = 1
    Z[-1] = 1
    Z = Z.transpose()
print(Z)