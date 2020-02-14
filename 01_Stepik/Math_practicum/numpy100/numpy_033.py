import numpy as np

print(np.arange('2005-02', '2005-03-02', dtype='datetime64[D]'))

start = np.datetime64(input(), 'D')
end = np.datetime64(input(), 'D')
Z = np.arange(start, end)
print(Z)