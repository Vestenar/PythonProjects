'''Имеется файл с данными по успеваемости абитуриентов.
Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой
и для каждого абитуриента выводит его среднюю оценку по этим трём предметам
на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы
по математике, физике и русскому языку по всем абитуриентам'''

journal = []

with open('c:\\adb\\dataset_3363_4.txt','r') as file:
    for i in file:
        journal += [i.strip().split(';')]

sr_pr1 = 0
sr_pr2 = 0
sr_pr3 = 0
for el in journal:
    print((int(el[1]) + int(el[2]) + int(el[3])) / 3)
    sr_pr1 += int(el[1])
    sr_pr2 += int(el[2])
    sr_pr3 += int(el[3])

print(sr_pr1/len(journal), sr_pr2/len(journal), sr_pr3/len(journal))
