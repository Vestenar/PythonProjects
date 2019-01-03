def checkPalindrome(inputString):
    nlen = len(inputString)
    if nlen == 1:
        t = True
    else:
        for i in range(nlen // 2):
            if inputString[i] == inputString[-i - 1]:
                t = True
            else:
                t = False

    return t

'''
Given the string, check if it is a palindrome.

Example

    For inputString = "aabaa", the output should be
    checkPalindrome(inputString) = true;
    For inputString = "abac", the output should be
    checkPalindrome(inputString) = false;
    For inputString = "a", the output should be
    checkPalindrome(inputString) = true.
'''