# def buildPalindrome(st):
#     rst = st[::-1]
#     tst = st
#     for i in range(1, len(st)):
#         if tst == tst[::-1]:
#             break
#         tst = st + rst[-i:]
#
#     return tst
def buildPalindrome(str):
    if str == str[::-1]:
        return str
    for i in range(len(str)):
        s = str + str[i::-1]
        if s == s[::-1]:
            return s


task = "abba"
print(buildPalindrome(task))

'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
'''