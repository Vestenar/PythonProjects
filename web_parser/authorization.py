import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "ru,en-US;q=0.7,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "PHPSESSID=sbe5jbr3nru2spccas0nkiute0; language=ru;"      # temporal cookie
}

data = {}
url = 'http://teamfinding.com/mynews'
url_log = 'http://teamfinding.com/account/login'

#TODO вынести хэдеры с обновляемым куки в файл конфигурации, логин и пароль, минимальную длину текста

def login():
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        print('AUTH NOT REQUIRED')
        return
    else:
        response_log = requests.post(url_log, headers=headers, data=data)
        headers['Cookie'] = f'PHPSESSID={response_log.cookies["PHPSESSID"]}; language=ru;'
        if response_log.json()['ok']:
            print("AUTHORIZATION SUCCESSFUL")


def send_message(send_to):

    url_message = "http://teamfinding.com/ru/message"
    message = '''#сидидома
                #берегитесебя
                '''
    params = {"PersonalMessage[FK_to_uid]": f"{send_to}", "PersonalMessage[text]": message}
    response = requests.post(url_message, headers=headers, data=params)
    message_log = open('messages_log.txt', 'a')
    if response.status_code == 200:
        print(f'Message to {send_to} successfully sent', file=message_log)
    else:
        print(f'ERROR: Try to send message to {send_to} manually', file=message_log)
    message_log.close()


    return response.status_code

