def sudoku(grid):
    for i in grid:  # check rows for non-unique
        if len(set(i)) != 9:
             return False

    for i in range(9):  # check columns for non-unique
        col = []
        for j in range(9):
            col.append(grid[j][i])
        if len(set(col)) != 9:
            return False

    for k in range(3):  # first 1/3 of grid
        for col in range(3):
            squ = set()
            for row in range(3):
                squ.update(grid[3*k+row][3*col:3*col+3])
            if len(squ) != 9:
                return False

    return True


task =  [[1,3,3,    5,4,6,  9,8,7],
         [4,6,5,    8,7,9,  3,2,1],
         [7,9,8,    2,1,3,  6,5,4],

         [9,2,1,    4,3,5,  8,7,6],
         [3,5,4,    7,6,8,  2,1,9],
         [6,8,7,    1,9,2,  5,4,3],

         [5,7,6,    9,8,1,  4,3,2],
         [2,4,3,    6,5,7,  1,9,8],
         [8,1,9,    3,2,4,  7,6,5]]

print(sudoku(task))

'''
Sudoku is a number-placement puzzle.
The objective is to fill a 9 × 9 grid with digits so that each column,
each row, and each of the nine 3 × 3 sub-grids that compose the grid
contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers
represents a correct solution to Sudoku.'''