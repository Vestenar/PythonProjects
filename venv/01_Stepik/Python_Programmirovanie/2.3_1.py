'''
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d+1):
    print('\t', i, end='')
print()

for i in range(a, b+1):
    print(i, end='')
    for j in range(c, d+1):
        print('\t', (j * i), end='')
    print()