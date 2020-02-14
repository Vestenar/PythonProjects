def mysum(lst):
    if not lst:
        return 0
    else:
        return nonempty(lst)


def nonempty(asd):
    return asd[0] + mysum(asd[1:])


s = [1,2,3,4,5,6]
print(mysum(s))