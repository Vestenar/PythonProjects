def front_back(a, b):
    i = (len(a) + 1) // 2
    j = (len(b) + 1) // 2
    return a[:i] + b[:j] + a[i:] + b[j:]


a = 'Kitten'
b = 'Donut'

print(front_back(a, b))

