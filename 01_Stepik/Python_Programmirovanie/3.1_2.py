'''Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
удаляет из него все нечётные значения, а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка'''

def modify_list(l):
    ans = []
    for i in l:
        if i%2 == 0:
            ans.append(i//2)
    l[:] = ans