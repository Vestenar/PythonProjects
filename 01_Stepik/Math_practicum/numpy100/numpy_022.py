import numpy as np

Y = np.array([[99, 11, 55],
            [33, 66, 99]])

Z = np.around((Y - Y.mean())/Y.std(), 2)
print(Z)