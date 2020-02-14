#САПЕР Stepik
n, m, k = (int(i) for i in input().split()) # строки, столбцы, кол-во мин
a = [[0 for j in range(m)] for i in range(n)]

for i in range(k): # ввод координат мин по одной
    row, col = (int(i) - 1 for i in input().split()) #выравнивает нумерацию строк и столбцов, теперь начинаются с 0
    a[row][col] = -1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di #позиция клетки плюс интервал +/- 1
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1: #проверка, что клетка для проверки еще в поле и в ней есть мина
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()