import requests


def request(login, password):
    data = {'login': login, 'password': password}
    response = requests.post('http://127.0.0.1:4000/other/auth', data=data)
    return response.text() == 'OK'
