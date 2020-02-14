import json, requests

with open('api_test.txt', 'r') as file:
    for number in file:
        number = number.strip()
        b = json.loads(requests.get(f'http://numbersapi.com/{number}/math?json=true').text)
        print('Interesting' if b['found'] else 'Boring')
