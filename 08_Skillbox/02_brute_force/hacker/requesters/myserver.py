import requests


def request(login, password):
    data = {'login': login, 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    return response.status_code == 200
