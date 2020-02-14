import numpy as np

Z = np.arange(11)

Z = np.where((Z > 3) & (Z < 9), -Z, Z)
print(Z)