def stringsRearrangement(inputArray):
    import itertools
    perm = list(itertools.permutations(inputArray, len(inputArray)))
    for k in perm:
        for i in range(1, len(k)):
            a = k[i]
            b = k[i-1]
            count = 0
            for index in range(len(a)):
                if a[index] != b[index]:
                    count += 1
            if count != 1:
                break
        if count == 1:
            return True
    return False


'''
Given an array of equal-length strings, check if it is possible to rearrange
the strings in such a way that after the rearrangement the strings at consecutive positions
would differ by exactly one character.

Example

    For inputArray = ["aba", "bbb", "bab"], the output should be
    stringsRearrangement(inputArray) = false.

    All rearrangements don't satisfy the description condition.

    For inputArray = ["ab", "bb", "aa"], the output should be
    stringsRearrangement(inputArray) = true.

    Strings can be rearranged in the following way: "aa", "ab", "bb".'''