def commonCharacterCount(s1, s2):
    n_count = 0
    for i in s1:
        if i in s2:
            n_count +=1
            s2 = s2.replace(i, "0", 1)
    return n_count

'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".'''