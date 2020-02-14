L1 = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
L2 = []
def flatter(l):
    for i in l:
        if isinstance(i, list):
            flatter(i)
        else:
            L2.append(i)
    return L2

flatter(L1)
print('Answer: ', L2)