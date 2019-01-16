def isSumOfConsecutive2(n):
    c = 0
    for i in range(1,n):
        s = i
        for j in range(i+1,n):
            s += j
            if s == n:
                c += 1
                break
            elif s > n:
                break
    return c
# def isSumOfConsecutive2(n): # решение через генератор
#     return sum([(2 * n) % i == 0 == (i + ((2 * n) // i) - 1) % 2 for i in range(2,int((2 * n) ** 0.5) + 1)])
n = 5
print(isSumOfConsecutive2(n))

'''
A couple of patterns to notice:
9 is a sum of
1.
ceil(9/2) - 1
ceil(9/2)
2.
ceil(9/3) - 1
ceil(9/3)
ceil(9/3) + 1

15 is a sum of
1.
ceil(15/2) - 1
ceil(15/2)
2.
ceil(15/3) - 1
ceil(15/3)
ceil(15/3) + 1
3.
ceil(15/5) - 2
ceil(15/5) - 1
ceil(15/5)
ceil(15/5) + 1
ceil(15/5) + 2
'''


'''
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

    For n = 9, the output should be
    isSumOfConsecutive2(n) = 2.

    There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

    For n = 8, the output should be
    isSumOfConsecutive2(n) = 0.

    There are no ways to represent n = 8.

'''
