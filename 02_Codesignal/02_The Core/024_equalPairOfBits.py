def equalPairOfBits(n, m):
    return 1 << '{0:032b}'.format(n^m)[::-1].index('0')


n = 1073741824
m = 1006895103
print('{0:032b}'.format(n))
print('{0:032b}'.format(m))
print(bin(n^m))
print('{0:032b}'.format(n^m))
print('{0:032b}'.format(n^m)[::-1])
print('{0:032b}'.format(n^m)[::-1].index('0'))

print((equalPairOfBits(n,m)))

'''
You're given two integers, n and m. Find position of the rightmost pair 
of equal bits in their binary representations (it is guaranteed that such a pair exists), 
counting from right to left.

Return the value of 2**position_of_the_found_pair (0-based).

Example

For n = 10 and m = 11, the output should be
equalPairOfBits(n, m) = 2.

10 = 1010, 11 = 1011, the position of the rightmost pair of equal bits 
is the bit at position 1 (0-based) from the right in the binary representations.
So the answer is 2**1 = 2.
'''
