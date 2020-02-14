def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
    #if rowsToDelete != []:
    for row in rowsToDelete[::-1]:
        matrix.pop(row)

    if columnsToDelete != []:
        for col in columnsToDelete[::-1]:
            for i in range(len(matrix)):
                matrix[i].pop(col)

    return matrix


a = [[1,2,3],[4,5,6],[7,8,9]]
r = []
k = [1,]

print(constructSubmatrix(a,r,k))




'''
Given a matrix (i.e. an array of arrays), find its submatrix obtained 
by deleting the specified rows and columns.

Example

For

matrix = [[1, 0, 0, 2], 
          [0, 5, 0, 1], 
          [0, 0, 3, 5]]

rowsToDelete = [1], and columnsToDelete = [0, 2], the output should be
constructSubmatrix(matrix, rowsToDelete, columnsToDelete) = [[0, 2],
                                                             [0, 5]]'''