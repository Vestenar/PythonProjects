'''#Вторая задача с request.
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
'''
import requests

with open('c:\\adb\\dataset_3378_3.txt') as inf:
    s1 = inf.readline().strip()
r = requests.get(s1).text
while r.strip().split()[0] != 'We':
    r = requests.get(s1[:s1.rindex('/')+1]+r).text
    print(r)
print(r)