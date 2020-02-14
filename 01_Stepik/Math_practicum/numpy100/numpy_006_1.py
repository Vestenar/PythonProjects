import numpy as np

M1 = np.array((
    (1., 2., 3., 0.),
    (4., 5., 6., 0.),
    (0., 1., 1., 6.),
    (7., 8., 9., 0.)
))

M2 = np.copy(M1)
print(M1[:,-2])

M2[-2] = np.sin(M1[-2] * np.pi / 6)

M2[:, -2] = np.exp(M2[:, -2])


print(repr(M2))
