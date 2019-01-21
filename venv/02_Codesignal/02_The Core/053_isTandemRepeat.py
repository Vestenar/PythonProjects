def isTandemRepeat(inputString):

    return inputString[:len(inputString)//2]*2 == inputString


print(isTandemRepeat("tandemtandem"))
'''
Determine whether the given string can be obtained by one concatenation of some string to itself.

Example

    For inputString = "tandemtandem", the output should be
    isTandemRepeat(inputString) = true;
    For inputString = "qqq", the output should be
    isTandemRepeat(inputString) = false;
    For inputString = "2w2ww", the output should be
    isTandemRepeat(inputString) = false.

'''
