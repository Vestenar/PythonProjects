def threeSplit(a):
    n = 0
    sum_thrd = sum(a)//3
    sum1 = 0
    for i in range(len(a)-2):
        sum1 += a[i]
        if sum1 == sum_thrd:
            sum2 = 0
            for j in range(i+1,len(a)-1):
                sum2 += a[j]
                if sum2 == sum_thrd:
                    n+=1
    return n


a = [0, -1, 0, -1, 0, -1]
print(threeSplit(a))
a = [-1, 1, -1, 1, -1, 1, -1, 1]
print(threeSplit(a))


'''
You have a long strip of paper with integers written on it in a single line 
from left to right. You wish to cut the paper into exactly three pieces such that 
each piece contains at least one integer and the sum of the integers in each piece is the same. 
You cannot cut through a number, i.e. each initial number will unambiguously belong to 
one of the pieces after cutting. How many ways can you do it?

It is guaranteed that the sum of all elements in the array is divisible by 3.

Example

For a = [0, -1, 0, -1, 0, -1], the output should be
threeSplit(a) = 4.

Here are all possible ways:

    [0, -1] [0, -1] [0, -1]
    [0, -1] [0, -1, 0] [-1]
    [0, -1, 0] [-1, 0] [-1]
    [0, -1, 0] [-1] [0, -1]

'''