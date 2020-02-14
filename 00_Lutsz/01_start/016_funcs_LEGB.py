def odd():
    funcs = []
    for i in 'abcdefg':
        funcs.append(lambda: i)
    return funcs

def normal():
    funcs = []
    for i in 'abcdefg':
        funcs.append(lambda i=i: i)     # именованные иргументы
    return funcs

for func in odd():
    print(func(), end='')       # ggggggg

print()

for func in normal():
    print(func(), end='')       # abcdefg
