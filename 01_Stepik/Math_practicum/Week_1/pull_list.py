out = []
def list_pull(L):
    for elem in L:
        if isinstance(elem, list):
            list_pull(elem)
        else:
            out.append(elem)
    return out

L = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]
print(list_pull(L))