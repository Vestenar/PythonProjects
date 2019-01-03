def absoluteValuesSumMinimization(a):

    list = {}

    for i in range(len(a)):
        sabs = 0
        for j in range(len(a)):
            sabs += abs(a[j] - a[-(i+1)])
        list[sabs] = a[-(i+1)]

    print(list)
    return list[min(list)]

'''
Given a sorted array of integers a, find an integer x from a such that the value of

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)

is the smallest possible (here abs denotes the absolute value).
If there are several possible answers, output the smallest one.'''