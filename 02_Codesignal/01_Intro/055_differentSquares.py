def differentSquares(matrix):
    row = len(matrix)
    col = len(matrix[0])
    rects = []
    for i in range(1,row):
        for j in range(1,col):
            rect = []
            for m in range(-1,1):
                for n in range(-1,1):
                    rect.append(matrix[i+m][j+n])
            if rect not in rects:
                rects.append(rect)
    return len(rects)

if __name__ == '__main__':

    assert differentSquares([[1,2,1],
                         [2,2,2],
                         [2,2,2],
                         [1,2,3],
                         [2,2,1]]) == 6, "1"

    assert differentSquares([[9,9,9,9,9],
                         [9,9,9,9,9],
                         [9,9,9,9,9],
                         [9,9,9,9,9],
                         [9,9,9,9,9],
                         [9,9,9,9,9]]) == 1, "2"

    assert differentSquares([[3]]) == 0, "3"

    assert differentSquares([[3,4,5,6,7,8,9]]) == 0, "4"

    assert differentSquares([[3],
                         [4],
                         [5],
                         [6],
                         [7]]) == 0, "5"

    assert differentSquares([[2,5,3,4,3,1,3,2],
                         [4,5,4,1,2,4,1,3],
                         [1,1,2,1,4,1,1,5],
                         [1,3,4,2,3,4,2,4],
                         [1,5,5,2,1,3,1,1],
                         [1,2,3,3,5,1,2,4],
                         [3,1,4,4,4,1,5,5],
                         [5,1,3,3,1,5,3,5],
                         [5,4,4,3,5,4,4,4]]) == 54, "6"
    
    assert differentSquares([[1,1,1,1,1,1,2,2,2,3,3,3,9,9,9,2,3,9]]) == 0, "7"

    print('You are awesome! All tests are done! Go Check it!')
'''
Given a rectangular matrix containing only digits, 
calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

    1 2
    2 2
    2 1
    2 2
    2 2
    2 2
    2 2
    1 2
    2 2
    2 3
    2 3
    2 1

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.array.integer matrix

    Guaranteed constraints:
    1 ≤ matrix.length ≤ 100,
    1 ≤ matrix[i].length ≤ 100,
    0 ≤ matrix[i][j] ≤ 9.

    [output] integer
        The number of different 2 × 2 squares in matrix.
'''