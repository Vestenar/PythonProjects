import numpy as np

Z = np.array([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [0, 0, 9]])
# Z = np.array([1, 2, 3, 4])

print(list(Z[(Z > 3).nonzero()]))