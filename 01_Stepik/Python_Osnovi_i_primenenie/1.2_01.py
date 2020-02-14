objects = [1, 2, 1, 2, 3]

print(len({id(i) for i in objects}))


