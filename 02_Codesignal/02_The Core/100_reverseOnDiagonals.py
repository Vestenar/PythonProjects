def reverseOnDiagonals(matrix):
    l = len(matrix)
    diag1 = [matrix[i][i] for i in range(l)][::-1]
    diag2 = [matrix[i][-i-1] for i in range(l)][::-1]
    for i in range(l):
        for j in range(l):
            if i == j:
                matrix[i][j] = diag1[i]
            elif j == l-i-1:
                matrix[i][j] = diag2[i]
    return matrix


matrix = [[43,455,32,103],
         [102,988,298,981],
         [309,21,53,64],
         [2,22,35,291]]
print(reverseOnDiagonals(matrix))
'''
The longest diagonals of a square matrix are defined as follows:

    the first longest diagonal goes from the top left corner to the bottom right one;
    the second longest diagonal goes from the top right corner to the bottom left one.

Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.

Example

For

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

the output should be

reverseOnDiagonals(matrix) = [[9, 2, 7],
                              [4, 5, 6],
                              [3, 8, 1]]

'''
