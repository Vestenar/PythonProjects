def sortByHeight(a):
    m = max(a)

    for i in range(1, len(a)):
        if a[-i] != -1:
            a[-i], a[a.index(m)] = a[a.index(m)], a[-i]
            m = max(a[:-i])
    return a


'''
Some people are standing in a row in a park. 
There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order 
without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].'''