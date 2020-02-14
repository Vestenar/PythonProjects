import numpy as np
np.random.seed(42)
nm =tuple(map(int, input().split()))
Z = np.random.random_sample(nm)
print(Z.mean())