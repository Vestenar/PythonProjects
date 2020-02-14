def starRotation(matrix, width, center, t):
    subm = []
    for i in range(width):
        subm.append(matrix[center[0]-width//2+i][center[1]-width//2:center[1]+width//2+1])
    star = [subm[width // 2], [subm[i][i] for i in range(width)], [subm[i][width // 2] for i in range(width)],
            [subm[i][width - i - 1] for i in range(width)]]
    for i in range(t % 8):
        star.insert(0, star.pop()[::-1])
    subm[width//2] = star[0]
    for i in range(width):
        subm[i][i] = star[1][i]
        subm[i][width//2] = star[2][i]
        subm[i][width-i-1] = star[3][i]
    for i in subm:
        print(i)
    for i in range(width):
        matrix[center[0]-width//2+i][center[1]-width//2:center[1]+width//2+1] = subm[i][:]
    return matrix


def starRotation2(m, w, c, t):  # решение перестановками
    for i in range(1,int((w+1)/2)):
        for _ in range(t%8):
            p = m[c[0]-i][c[1]-i]
            m[c[0]-i][c[1]-i] = m[c[0]][c[1]-i]
            m[c[0]][c[1]-i] = m[c[0]+i][c[1]-i]
            m[c[0]+i][c[1]-i] = m[c[0]+i][c[1]]
            m[c[0]+i][c[1]] = m[c[0]+i][c[1]+i]
            m[c[0]+i][c[1]+i] = m[c[0]][c[1]+i]
            m[c[0]][c[1]+i] = m[c[0]-i][c[1]+i]
            m[c[0]-i][c[1]+i] = m[c[0]-i][c[1]]
            m[c[0]-i][c[1]] = p
    return m


def starRotation3(matrix, width, center, t):  # векторное решение
    [r, c] = center
    offset = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    print(offset)
    for d in range(1, width // 2 + 1):
        v = [matrix[r + d * i][c + d * j] for (i, j) in offset]
        v = v[-(t % 8):] + v[:-(t % 8)]
        for o, (i, j) in enumerate(offset):
            matrix[r + d * i][c + d * j] = v[o]

    return matrix


matrix = [[1, 0, 0, 2, 0, 0, 3],
          [0, 1, 0, 2, 0, 3, 0],
          [0, 0, 1, 2, 3, 0, 0],
          [8, 8, 8, 9, 4, 4, 4],
          [0, 0, 7, 6, 5, 0, 0],
          [0, 7, 0, 6, 0, 5, 0],
          [7, 0, 0, 6, 0, 0, 5]]
width = 7
center = [3, 3]
t = 1
print(starRotation(matrix,width,center,t))

'''
Consider a (2k+1) × (2k+1) square subarray of an integer integers matrix. Let's call the union of the square's two longest diagonals, middle column and middle row a star. Given the coordinates of the star's center in the matrix and its width, rotate it 45 · t degrees clockwise preserving position of all matrix elements that do not belong to the star.

Example

    For

    matrix = [[1, 0, 0, 2, 0, 0, 3],
              [0, 1, 0, 2, 0, 3, 0],
              [0, 0, 1, 2, 3, 0, 0],
              [8, 8, 8, 9, 4, 4, 4],
              [0, 0, 7, 6, 5, 0, 0],
              [0, 7, 0, 6, 0, 5, 0],
              [7, 0, 0, 6, 0, 0, 5]]

    width = 7, center = [3, 3] and t = 1, the output should be

    starRotation(matrix, width, center, t) = [[8, 0, 0, 1, 0, 0, 2],
                                              [0, 8, 0, 1, 0, 2, 0],
                                              [0, 0, 8, 1, 2, 0, 0],
                                              [7, 7, 7, 9, 3, 3, 3],
                                              [0, 0, 6, 5, 4, 0, 0],
                                              [0, 6, 0, 5, 0, 4, 0],
                                              [6, 0, 0, 5, 0, 0, 4]]

    For

    matrix = [[1, 0, 0, 2, 0, 0, 3],
              [0, 1, 0, 2, 0, 3, 0],
              [0, 0, 1, 2, 3, 0, 0],
              [8, 8, 8, 9, 4, 4, 4],
              [0, 0, 7, 6, 5, 0, 0]]

    width = 3, center = [1, 5] and t = 81, the output should be

    starRotation(matrix, width, center, t) = [[1, 0, 0, 2, 0, 0, 0],
                                              [0, 1, 0, 2, 3, 3, 3],
                                              [0, 0, 1, 2, 0, 0, 0],
                                              [8, 8, 8, 9, 4, 4, 4],
                                              [0, 0, 7, 6, 5, 0, 0]]


'''
