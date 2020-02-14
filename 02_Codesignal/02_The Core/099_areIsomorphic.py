def areIsomorphic(array1, array2):

    return len(array1) == len(array2) and all([len(array1[i]) == len(array2[i]) for i in range(len(array2))])


array1 = [[1,3,4],
 [1]]
array2 = [[2,1,2],
 []]
print(areIsomorphic(array1, array2))

'''
Two two-dimensional arrays are isomorphic if they have the same number of rows 
and each pair of respective rows contains the same number of elements.

Given two two-dimensional arrays, check if they are isomorphic.

Example

    For

    array1 = [[1, 1, 1],
              [0, 0]]

    and

    array2 = [[2, 1, 1],
              [2, 1]]

    the output should be
    areIsomorphic(array1, array2) = true;

    For

    array1 = [[2],
              []]

    and

    array2 = [[2]]

    the output should be
    areIsomorphic(array1, array2) = false.

'''
