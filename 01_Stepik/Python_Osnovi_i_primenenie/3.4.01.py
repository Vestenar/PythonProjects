import requests
import re

res = requests.get("https://docs.python.org/3.5/")
print(res.status_code)
print(res.headers["server"])
# print(res.text)

res = requests.get("https://docs.python.org/3.5/_static/py.png")
print(res.content)

with open (r'c:\adb\python.png', 'wb') as pict:  # запись в файл бинарных данных
    pict.write(res.content)