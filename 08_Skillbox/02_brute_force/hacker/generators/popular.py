state = 0

with open('generators/pop-passwords.txt') as passwords_file:
    passwords = [password.strip() for password in passwords_file.readlines()]


def next_str():
    global state
    login = passwords[state]
    finished = state == len(passwords) - 1

    if finished:
        state = 0
    else:
        state += 1

    return login, finished
