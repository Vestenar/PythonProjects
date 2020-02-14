# Name 	stepik_app
# Client Id 	574bc8ace443884b8ed3
# Client Secret 	b70a312959780999a92787c124a4fedc

import requests
import json
import pprint

client_id = '574bc8ace443884b8ed3'
client_secret = 'b70a312959780999a92787c124a4fedc'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI1ZTA3YmM3YmMxZDM4" \
        "NzAwMGU3NTkwOTIiLCJleHAiOjE1NzgxNzAxMDgsImlhdCI6MTU3NzU2NTMwOCwiYXVkIjoiNWUwN2JjN2JjMWQzODcwMDBlNzU5MDky" \
        "IiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjVlMDdiYzdjMmYwMDQ5MDAxNjdiMTliYSJ9._yO---DsnrkZFGnro95k8OP1BUZE37ga3iePLoXAgKE"

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

# инициируем запрос с заголовком
id = '4d8b92b34eb68a1b2c0003f4'
r = requests.get(f"https://api.artsy.net/api/artists/{id}", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)
pprint.pprint(j)

artlist = {}
with open('api_test_artsy.txt', 'r') as file:
    for name in file:
        name = name.strip()
        r = requests.get(f"https://api.artsy.net/api/artists/{name}", headers=headers)
        r.encoding = 'utf-8'
        r = json.loads(r.text)
        pprint.pprint(r)
        date = int(r['birthday'])
        artname = r['sortable_name']
        if date not in artlist:
            artlist.update({date: [artname]})
        else:
            artlist[date] += [artname]
pprint.pprint(artlist)
with open('result.txt', 'w') as result:
    for year, names in sorted(artlist.items()):
        for name in sorted(names):
            result.write(name + '\n')