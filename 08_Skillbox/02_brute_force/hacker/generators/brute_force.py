state = 0
digits_count = 0
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'


def next_str():
    global state
    global digits_count

    n = state
    base = len(alphabet)
    result = ''
    while len(result) < digits_count:
        rest = n % base
        result = alphabet[rest] + result
        n = n // base

    # проверить пора ли добавлять цифру
    # более топорный способ - all(char == alphabet[-1] for char in result):
    state += 1
    if state == base ** digits_count:
        state = 0
        digits_count += 1

    return result, False
