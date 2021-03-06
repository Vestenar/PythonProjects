'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно.
В фамилии нет пробелов, а в качестве роста используется натуральное число,
но при подсчёте среднего требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса
(для классов с первого по одиннадцатый).
Если про какой-то класс нет информации, необходимо вывести напротив него прочерк
'''


rost = {a: [] for a in range(1, 12)}
with open(r'C:\\adb\\tabl_rost.txt') as inf:
    for line in inf:
        text = line.strip().split()
        rost[int(text[0])] += [int(text[2])]
for key, value in rost.items():
    if value == []:
        print(key, '-')
    else:
        print(key, sum(value)/len(value))

''''#еще одно решение
with open('C:\\adb\\tabl_rost.txt') as inf:
    text = inf.readlines()
dic = {}
for a in text:
    x = a.strip().split()
    dic.setdefault(int(x[0]), []).append(int(x[2]))
for i in range(1,len(dic)):
    print(i, sum(dic[i])/len(dic[i]) if i in dic.keys() else '-')'''

