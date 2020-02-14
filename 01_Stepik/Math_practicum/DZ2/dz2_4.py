

L1 = [1, ['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]

def copy(l, n_l=[]):
    new_l = []
    for lst in l:
        if not isinstance(lst, list):
            new_l.append(lst)
        else:
            new_l+=([copy(lst, n_l)])
    return new_l



L2 = copy(L1)
print(L1)
print(L2)
print(L1 == L2)
L1[1][0] = 'fcre'
print(L1)
print(L2)