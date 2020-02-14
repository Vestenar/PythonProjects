import generators
import requesters

login_generator = generators.logins
password_generator = generators.brute_force
requester = requesters.myserver
result_filename = 'result.txt'

passwords_finished = False
while not passwords_finished:
    password, passwords_finished = password_generator.next_str()

    logins_finished = False
    while not logins_finished:
        login, logins_finished = login_generator.next_str()

        if requester.request(login, password):
            result = f'login generator "{login_generator.__name__}" ' \
                     f'password generator "{password_generator.__name__}" ' \
                     f'requester "{requester.__name__}" ' \
                     f'{login=} {password=}'
            print(result)
            with open(result_filename, 'a') as f:
                f.write(result)
                f.write('\n')
