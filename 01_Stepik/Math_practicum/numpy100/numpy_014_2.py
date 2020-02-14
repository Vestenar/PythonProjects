import numpy as np
np.random.seed(42)
nm =tuple(map(int, input().split()))
Z = np.random.random_sample(nm)
print(Z)
zmin = 1
zmax = 0
for i in range(len(Z[0])):
    a = (Z[:,i].mean())
    if a > zmax: zmax = a
    if a < zmin: zmin = a
print(zmin, zmax, sep='\n')
