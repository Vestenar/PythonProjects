def minesweeper(matrix):
    row, col = len(matrix), len(matrix[0])
    ans = [[0 for c in range(col)] for r in range(row)]

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == True:
                ans[i][j] = -1
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < row and 0 <= aj < col and matrix[ai][aj] == True:
                        ans[i][j] += 1
    return ans


'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]

the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
'''