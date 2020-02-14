'''
Напишите программу, которая принимает на вход список чисел в одной строке и
выводит на экран в одну строку значения, которые повторяются в нём более одного раза.
'''

a = [int(i) for i in input().split()]
b = []
for i in range(len(a)):
    if a.count(a[i]) > 1 and (a[i] not in b):
        b.append(a[i])

for i in b:
    print(i, end = ' ')