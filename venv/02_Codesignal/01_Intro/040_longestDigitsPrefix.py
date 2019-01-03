def longestDigitsPrefix(inp):
    import re
    ans = ''
    nums = re.findall(r'\d+', inp)
    for i in nums:
        if inp[inp.find(i)-1] == ' ':
            inp = inp[inp.find(i)+len(i):]
        else:
            if len(i) > len(ans):
                ans = i
    return ans

if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longestDigitsPrefix("123aa1") == "123", "First"
    assert longestDigitsPrefix("0123456789") == "0123456789", "Second"
    assert longestDigitsPrefix("  3) always check for whitespaces") is "", "Third"
    assert longestDigitsPrefix("12abc34") =="12", "Fourth"
    assert longestDigitsPrefix("the output is 42") == "", "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

'''#
def longestDigitsPrefix(inputString):
    return re.findall('^\d*',inputString)[0]
'''

'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString="123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
'''