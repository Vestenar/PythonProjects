def polygonPerimeter(matrix):
    n = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                n += 4
                for di in [-1, 1]:
                    ai = i + di
                    if 0 <= ai < len(matrix) and matrix[ai][j]:
                        n -= 1
                for dj in [-1, 1]:
                    aj = j + dj
                    if 0 <= aj < len(matrix[0]) and matrix[i][aj]:
                        n -= 1
    return n


matrix = [[False, True,  True ],
          [True,  True,  False],
          [True,  False, False]]

print(polygonPerimeter(matrix))
'''
You have a rectangular white board with some black cells. 
The black cells create a connected black figure, i.e. it is possible 
to get from any black cell to any other one through connected adjacent 
(sharing a common side) black cells.

Find the perimeter of the black figure assuming that a single cell has unit length.

It's guaranteed that there is at least one black cell on the table.

Example

    For

    matrix = [[false, true,  true ],
              [true,  true,  false],
              [true,  false, false]]

    the output should be
    polygonPerimeter(matrix) = 12.

    For

    matrix = [[true, true,  true],
              [true, false, true],
              [true, true,  true]]

    the output should be
    polygonPerimeter(matrix) = 16.

'''