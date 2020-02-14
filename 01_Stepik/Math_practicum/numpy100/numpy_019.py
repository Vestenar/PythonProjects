import numpy as np

n, m = map(int, input().split())
Z = np.tile(np.array([[0, 1], [1, 0]]), (n, m))[:n, :m]

print(Z)