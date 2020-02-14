def contoursShifting(matrix):
    sub = []
    h = len(matrix)
    w = len(matrix[0])
    if h == 1 and w == 1: return matrix
    if w == 1:
        matrix.insert(0, matrix.pop())
        return matrix
    if h == 1:
        matrix[0].insert(0, matrix[0].pop())
        return matrix
    while h > 1 and w > 1:
        sub.append(matrix[0] + [matrix[i][-1] for i in range(1, h-1)] +
                    matrix[-1][::-1] + [matrix[i][0] for i in range(1, h-1)][::-1])

        h -= 2
        w -= 2
        try:
            del matrix[0], matrix[-1]
            for i in range(h-2):
                del matrix[i][0]
                del matrix[i][-1]
        except:
            break
        # print(sub)
        # print("rest of matrix")
        # for i in matrix:
        #     print(i)
        # print()
        print(h,w)
    if w == 1 and h > 1:
        matrix.insert(-1, matrix.pop(0))
    if h == 1 and w > 1:
        matrix[0].insert(-1, matrix[0].pop(0))
    print(matrix)
    for i in sub:
        i.insert(sub.index(i) % 2 * len(i), i.pop(sub.index(i) % 2 - 1))
    print(sub)
    # if not matrix[0]: matrix = []
    for i in range(len(sub)):
        t = sub.pop()
        matrix.insert(0, t[:w+1])
        # print(matrix)
        matrix.append(t[len(t) // 2:len(t) // 2 + w + 1][::-1])
        for j in range(h+1):
            matrix[j].append(t[w + 1 + j])
            matrix[len(matrix)-j-1].insert(0,t[len(t) // 2 + w + j+1])
        # print(matrix)
        h += 2
        w += 2

    # print(sub)

    return matrix
matrix = [[1,2,3],
 [6,7,8],
 [11,12,13],
 [16,17,18],
 [21,22,23],
 [24,25,26]]
# matrix =    [[ 1, 2, 3, 4],
#              [ 5, 6, 7, 8],
#              [ 9,10,11,12],
#              [13,14,15,16]]
# matrix =    [[ 1, 2, 3, 4],
#              [ 5, 6, 7, 8],
#              [ 9,10,11,12],
#              [13,14,15,16],
#              [17,18,19,20]]
# matrix = [[1,2,3,4,5],
#  [6,7,8,9,10],
#  [11,12,13,14,15],
#  [16,17,18,19,20]]
# matrix = [[ 1,  2,  3,  4,  5,  6,  7,  8, 0],
#           [ 9, 10, 11, 12, 13, 14, 15, 16, 2],
#           [17, 18, 19, 20, 21, 22, 23, 24, 0],
#           [25, 26, 27, 28, 29, 30, 31, 32, 4],
#           [33, 34, 35, 36, 37, 38, 39, 40, 0],
#           [41, 42, 43, 44, 45, 46, 47, 48, 5],
#           [49, 50, 51, 52, 53, 54, 55, 56,89],
#           [57, 58, 59, 60, 61, 62, 63, 64, 0],
#           [ 0,  0, 99,  0,  0,  8,  0,  0,77]]

print(contoursShifting(matrix))


# работает для квадратных матриц
# n = len(matrix) // 2 - 1
# while n >= 0 and m >= 0:
#     sub = []
#     sub.append(matrix[n][m:(len(matrix) - m - 1)])
#     print(sub)
#     # sub.append([matrix[n + i][-1 - m] for i in range(0, len(matrix) - 2 * n - 1)])
#
#     sub.append(matrix[len(matrix) - n - 1][m + 1:(len(matrix) - m)][::-1])
#     print(sub)
#     # sub.append([matrix[n + i][m] for i in range(1, len(matrix) - 2 * n)][::-1])
#
#     sub.insert(n % 2 * len(sub), sub.pop(n % 2 - 1))
#     # print(sub)
#     print()
#     n -= 1
#     m -= 1
#
#     if n%2 == 0:
#         for i in range(1+n, len(matrix)-n):
#             matrix[i].insert(-(1+n), (matrix[i-(1+n)].pop()))
#         matrix[-(1+n)].insert(len(matrix)-n, matrix[-(1+n)].pop(-1-(1+n)))
#         for i in range(n, len(matrix)-1-n):
#             matrix[i].insert(0, (matrix[i+1].pop(0)))
# else:
# for i in range(1+n, len(matrix)-n):
#     matrix[i].insert(-(1+n), (matrix[i-1].pop()))
# matrix[-1].insert(len(matrix)-n, matrix[-1].pop(-2))
# for i in range(n, len(matrix)-1-n):
#     matrix[i].insert(0, (matrix[i+1].pop(0)))

'''
Mark got a rectangular array matrix for his birthday, and now he's thinking about all the fun things he can do with it. He likes shifting a lot, so he decides to shift all of its i-contours in a clockwise direction if i is even, and counterclockwise if i is odd.

Here is how Mark defines i-contours:

    the 0-contour of a rectangular array as the union of left and right columns as well as top and bottom rows;
    consider the initial matrix without the 0-contour: its 0-contour is the 1-contour of the initial matrix;
    define 2-contour, 3-contour, etc. in the same manner by removing 0-contours from the obtained arrays.

Implement a function that does exactly what Mark wants to do to his matrix.

Example

    For

    matrix = [[ 1,  2,  3,  4],
               [ 5,  6,  7,  8],
               [ 9, 10, 11, 12],
               [13, 14, 15, 16],
               [17, 18, 19, 20]]

    the output should be

    contoursShifting(matrix) = [[ 5,  1,  2,  3],
                                 [ 9,  7, 11,  4],
                                 [13,  6, 15,  8],
                                 [17, 10, 14, 12],
                                 [18, 19, 20, 16]]

    For matrix = [[238, 239, 240, 241, 242, 243, 244, 245]],
    the output should be
    contoursShifting(matrix) = [[245, 238, 239, 240, 241, 242, 243, 244]].

    Note, that if a contour is represented by a 1 × n array, its center is considered to be below it.

    For

    matrix = [[238],
               [239],
               [240],
               [241],
               [242],
               [243],
               [244],
               [245]]

    the output should be

    contoursShifting(matrix) = [[245],
                                 [238],
                                 [239],
                                 [240],
                                 [241],
                                 [242],
                                 [243],
                                 [244]]

    If a contour is represented by an n × 1 array, its center is considered to be to the left of it.

'''
