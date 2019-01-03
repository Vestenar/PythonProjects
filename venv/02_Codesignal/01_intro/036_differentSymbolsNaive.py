def differentSymbolsNaive(s):
    dict = {}
    for i in s:
        if i not in dict:
            dict[i] = 1
    return len(dict)

'''
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c.'''