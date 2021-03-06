def swapDiagonals(matrix):
    l = len(matrix)
    diag1 = [matrix[i][i] for i in range(l)]
    diag2 = [matrix[i][-i-1] for i in range(l)]
    for i in range(l):
        for j in range(l):
            if i == j:
                matrix[i][j] = diag2[i]
            elif j == l-i-1:
                matrix[i][j] = diag1[i]
    return matrix


matrix=[[1,2,3],
 [4,5,6],
 [7,8,9]]
print(swapDiagonals(matrix))


'''
The longest diagonals of a square matrix are defined as follows:

    the first longest diagonal goes from the top left corner to the bottom right one;
    the second longest diagonal goes from the top right corner to the bottom left one.

Given a square matrix, your task is to swap its longest diagonals by exchanging 
their elements at the corresponding positions.

Example

For

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

the output should be

swapDiagonals(matrix) = [[3, 2, 1],
                         [4, 5, 6],
                         [9, 8, 7]]

'''