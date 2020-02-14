def areSimilar(a, b):
    idx = []
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            idx.append(i)
    if len(idx) == 0:
        return True
    if len(idx) != 2:
        return False
    if a[idx[0]] == b[idx[1]] and a[idx[1]] == b[idx[0]]:
        return True
    else:
        return False

'''
Two arrays are called similar if one can be obtained from another by swapping 
at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

    For a = [1, 2, 3] and b = [1, 2, 3], the output should be
    areSimilar(a, b) = true.

    The arrays are equal, no need to swap any elements.

    For a = [1, 2, 3] and b = [2, 1, 3], the output should be
    areSimilar(a, b) = true.

    We can obtain b from a by swapping 2 and 1 in b.

    For a = [1, 2, 2] and b = [2, 1, 1], the output should be
    areSimilar(a, b) = false.

    Any swap of any two elements either in a or in b won't make a and b equal.
'''