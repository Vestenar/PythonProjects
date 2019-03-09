from functools import reduce

s = map(pow, [1, 2, 3], [2, 3, 4])
print(list(s))

s = map(lambda x, y: x ** y, [1, 2, 3], [2, 3, 4])
print(list(s))

f = filter(lambda x: type(x) == int, [1,2,"1","2"])
print(list(f))

a = reduce((lambda x, y: x + y), [1, 2, 3, 4])
print(a)