'''
Выведите таблицу размером n×n, заполненную числами
от 1 до n**2 по спирали, выходящей из левого верхнего угла и закрученной
по часовой стрелке, как показано в примере (здесь n=5):
'''

m = int(input())
mx = [[0 for i in range(m)]for j in range(m)]
cnt = 1
for i in range(m):
    mx[0][i] = cnt
    cnt += 1
n = m-1
while cnt < m**2:
    for j in range(m//2):
        for i in range(n):
            mx[i+j+1][m-j-1] = cnt
            cnt +=1
        for i in range(n):
            mx[m-j-1][m-j-i-2] = cnt
            cnt +=1
        n -=1
        for i in range(n):
            mx[m-j-i-2][j] = cnt
            cnt += 1
        for i in range(n):
            mx[j+1][j+i+1] = cnt
            cnt+=1
        n -=1


for i in range(m):
    for j in range(m):
        print(mx[i][j], end=' ')
    print()

''' #решение из комментариев
n = int(input())
x,y,b,a,t = 0,0,0,1, [[0]*n for i in range(n)]
for i in range(n*n):
    t[x][y]=i+1
    if t[(x+b)%n][(y+a)%n]!=0: b,a=a,-b
    x,y=x+b,y+a
[print(*i) for i in t]
'''

#еще ожно решение с вращением матрицы
'''
def rotate_matrix(matrix):
    """
    Функция для вращения квадратной матрицы $n\times n$ (список из $n$ списков по $n$ элементов)
    против часовой стрелки.
    
    Пример работы:
    [[1 2 3]     [[1 0 0]
     [0 0 0]  ->  [2 0 0] 
     [0 0 0]]     [3 0 0]]
    
    """
    return [list(i) for i in list(zip(*matrix))[::-1]] # list(zip(*matrix))[::-1] возвращает список кортежей,
                                                       # но в дальнейшем нужны списки. 
n = int(input())

matrix = [[0]*n for i in range(n)]             # Инициализация матрицы $n\times n$ нулями.
numbers_list = [n for n in range(1, n**2 + 1)] # Список из которого будут браться числа для заполнения матрицы.
pos_in_numbers_list = 0                        # Индекс текущего числа в списке
number_of_rotations = 0                        # Число поворотов матрицы
row_pos = 0                                    # Текущая строка матрицы

while row_pos < (n//2 + 1):
    while number_of_rotations < 4:
        for col in range(n):
            if matrix[row_pos][col] == 0:
                matrix[row_pos][col] = numbers_list[pos_in_numbers_list]
                pos_in_numbers_list += 1
        matrix = rotate_matrix(matrix)
        number_of_rotations += 1
        col_pos = 0
    number_of_rotations = 0
    row_pos += 1

for i in range(n):
    print(*matrix[i])
    '''