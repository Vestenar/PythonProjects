def mysum(lst):
    print(lst)
    if not lst:
        return 0
    else:
        return lst[0] + mysum(lst[1:])


s = [1,2,3,4,5,6,7,8,9]
mysum(s)
