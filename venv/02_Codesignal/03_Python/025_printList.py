def printList(lst):
    return 'This is your list: '+str(lst)

def printList2(lst):
    return "This is your list: {}".format(lst)

lst = [-74, -71, -7, -88, 13, -22, 7, 7, 71, 28, -78, -17, 77, 10]
print(printList(lst))
print(printList2(lst))