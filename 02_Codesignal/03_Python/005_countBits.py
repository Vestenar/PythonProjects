def countBits(n):
    return n.bit_length()

print(countBits(50))
'''
Implement a function that, given an integer n, 
uses a specific method on it and returns the number of bits in its binary representation.

Example

For n = 50, the output should be
countBits(n) = 6.

50 = 110010, a number that consists of 6 digits. Thus, the output should be 6.
'''
