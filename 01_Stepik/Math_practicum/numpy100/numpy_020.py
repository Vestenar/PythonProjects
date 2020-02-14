import numpy as np

i = 4
Z = np.array([[[ 1,  2],
        [ 3,  4]],

       [[11, 12],
        [13, 14]]])

print(np.unravel_index(i, Z.shape))