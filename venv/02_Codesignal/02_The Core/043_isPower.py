# def isPower(n):
#     if n == 1:
#         return True
#     for i in range(2,n):
#         if (n**(1/i)) == int(n**(1/i)):
#             print(i)
#             return True
#         if n**(1/i) < 1:
#             break
#     return False
import math
def isPower(n):
    if n == 1:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        for k in range(2,int(math.sqrt(n))+1):
            if math.pow(i,k) == n:
                return True
    return False
print(isPower(324))

'''
Determine if the given number is a power of some non-negative integer.

Example

    For n = 125, the output should be
    isPower(n) = true;
    For n = 72, the output should be
    isPower(n) = false.

'''
