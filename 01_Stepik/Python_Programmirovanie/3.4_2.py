'''
Напишите программу, которая считывает текст из файла
(в файле может быть больше одной строки) и выводит самое частое слово в этом тексте
и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
'''


s = ''
with open('C:\\adb\\dataset_3363_3.txt') as inf:
    for line in inf:
        s += line.strip().lower() + ' '
a = []
a =s.split()
dict = {}
for i in a:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
maxword, count = "", 0
for word in dict:
    if dict[word] > count or dict[word] == count and word < maxword:
        maxword, count = word, dict[word]
print(maxword + ' ' +str(count))
