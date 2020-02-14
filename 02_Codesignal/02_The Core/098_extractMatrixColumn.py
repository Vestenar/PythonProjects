def extractMatrixColumn(matrix, column):

    return [mat[column] for mat in matrix]


matrix =   [[1,1,1,2],
            [0,5,0,4],
            [2,1,3,6]]
column = 2
print(extractMatrixColumn(matrix, column))