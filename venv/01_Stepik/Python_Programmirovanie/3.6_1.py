'''Скачайте файл. В нём указан адрес другого файла,
который нужно скачать с использованием модуля requests и посчитать число строк в нём.
'''
import requests
with open('c:\\adb\\dataset_3378_2.txt') as inf:
    s1 = inf.readline().strip()
r = requests.get(s1).text.splitlines()
print(len(r))



