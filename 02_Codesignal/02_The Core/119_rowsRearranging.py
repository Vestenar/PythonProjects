def rowsRearranging(matrix):
    if len(matrix) == 1:
        return True
    for i in range(len(matrix[0])):
        matrix.sort(key=lambda x: x[i])
        for col in range(len(matrix[0])):
            a = [matrix[row][col] for row in range(len(matrix))]
            if a == sorted(a):
                continue
            else:
                break
        else: return True

    return False




matrix = [[0,1,3],
         [1,2,6],
         [2,3,-1],
         [-1,4,-2]]
print(rowsRearranging(matrix))
matrix = [[6,4],
 [2,2],
 [4,3]]
print(rowsRearranging(matrix))

matrix = [[-186,169,47,28,275,67,-118,-9,162],
 [-296,269,-261,54,253,213,300,-52,-124],
 [175,-205,-217,-114,-170,266,230,-38,-138],
 [-298,295,124,-277,-279,-243,-218,-206,148],
 [12,8,-221,-190,-175,-299,244,-169,-66],
 [36,294,229,-144,218,19,-166,169,264]]
print(rowsRearranging(matrix))