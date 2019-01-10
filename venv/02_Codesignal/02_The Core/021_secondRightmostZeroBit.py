def secondRightmostZeroBit(n):
    return 2**(bin((n|(1<<(bin(n)[::-1].index("0")))))[::-1].index("0"))


n = 1073741824

print(bin(n))
print(bin(1073741825))
print(bin(n)[::-1])
print(bin(n)[::-1].index("0"))
print(bin(n|(1<<(bin(n)[::-1].index("0")))))
print(bin((n|(1<<(bin(n)[::-1].index("0")))))[::-1].index("0"))


'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.

Presented with the integer n, find the 0-based position of the second rightmost 
zero bit in its binary representation (it is guaranteed that such a bit exists), counting from right to left.

Return the value of 2position_of_the_found_bit.

Example

For n = 37, the output should be
secondRightmostZeroBit(n) = 8.

37 = 100101. The second rightmost zero bit is at position 3 (0-based) from the right in the binary representation of n.
Thus, the answer is 2**3 = 8.'''
