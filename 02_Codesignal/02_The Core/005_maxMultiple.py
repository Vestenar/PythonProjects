# def maxMultiple(divisor, bound):
#     n = 0
#     for i in range(bound, 0, -1):
#         if i % divisor == 0:
#             n = i
#             break
#     return n


def maxMultiple(divisor, bound):
    return bound - (bound % divisor)

print(maxMultiple(7,100))
'''
Given a divisor and a bound, find the largest integer N such that:

    N is divisible by divisor.
    N is less than or equal to bound.
    N is greater than 0.

It is guaranteed that such a number exists.

Example

For divisor = 3 and bound = 10, the output should be
maxMultiple(divisor, bound) = 9.

The largest integer divisible by 3 and not larger than 10 is 9.
'''