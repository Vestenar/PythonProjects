def alphabeticShift(inputString):
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    ans = ''
    for i in range(len(inputString)):
        n = int(alphabet.index(inputString[i])) + 1
        if n > 25:
            n = 0
        ans += alphabet[n]
    return ans

'''
Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).

Example

For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".
'''