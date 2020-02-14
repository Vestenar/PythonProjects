import numpy as np
np.random.seed(42)
n,m = map(int, input().split())
Z = np.random.random_sample((n,m))
print(Z.min(),Z.max(), sep='\n')
