def isLucky(n):
    n = str(int(n))
    mid = len(n)//2
    n1 = n[:mid]
    n2 = n[mid:]
    sum1 = 0
    for i in range(len(n1)):
        sum1 +=int(n1[i])
    for i in range(len(n2)):
        sum1 -=int(n2[i])

    return sum1 == 0

'''
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the digits 
is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    isLucky(n) = true;
    For n = 239017, the output should be
    isLucky(n) = false.
'''