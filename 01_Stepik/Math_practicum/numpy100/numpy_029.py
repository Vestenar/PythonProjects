import numpy as np


A = np.array([-3.1, -5.9, 0, 2.2, 9.8])
A = np.where((A < 0), np.floor(A), np.ceil(A))
# A = np.where((A > 0), np.ceil(A), A)
print(A)