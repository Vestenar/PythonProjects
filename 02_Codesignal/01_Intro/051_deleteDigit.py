def deleteDigit(n):
    n = str(n)
    ma = 0
    for i in range(len(n)):
        k = n[:i] + n[i+1:]
        if int(k) > ma:
            ma = int(k)
    return ma

task = 222219
print(deleteDigit(task))

'''
Given some integer, find the maximal number you can obtain
by deleting exactly one digit of the given number.

Example

    For n = 152, the output should be
    deleteDigit(n) = 52;
    For n = 1001, the output should be
    deleteDigit(n) = 101.
'''