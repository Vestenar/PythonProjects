state = 0
logins = ['admin', 'adsdasa', '12345', 'cat']


def next_str():
    global state
    login = logins[state]
    finished = state == len(logins) - 1

    if finished:
        state = 0
    else:
        state += 1

    return login, finished
