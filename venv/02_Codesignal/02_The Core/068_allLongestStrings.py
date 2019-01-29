def allLongestStrings(inputArray):

    out = []

    for i in range(len(inputArray)):
        if len(inputArray[i]) == max(len(s) for s in inputArray):
            out.append(inputArray[i])

    return out