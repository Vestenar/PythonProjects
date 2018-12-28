def allLongestStrings(inputArray):
    lenw = 0
    out = []

    for i in range(len(inputArray)):
        if len(inputArray[i]) == max(len(s) for s in inputArray):
            out.append(inputArray[i])

    return out

'''Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
'''