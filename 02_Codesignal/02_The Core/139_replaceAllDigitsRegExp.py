import re
def replaceAllDigitsRegExp(inputString):
    return re.sub("\d", "#", inputString)


input = "There are 12 points"
print(replaceAllDigitsRegExp(input))
'''
Implement a function that replaces each digit in the given string with a '#' character.

Example

For input = "There are 12 points", the output should be
replaceAllDigitsRegExp(input) = "There are ## points".
'''