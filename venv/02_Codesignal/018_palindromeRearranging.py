def palindromeRearranging(inputString):
    a = []
    for i in range(len(inputString)):
        if inputString.count(inputString[i]) % 2 != 0:
            if inputString[i] != inputString[i-1]:
                a.append(inputString.count(inputString[i]))


    return len(a) <= 1

'''Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''