phone_book = {}

for _ in range(int(input())):
    command, *abonent = input().split()
    if command == 'add':
        phone_book[abonent[0]] = abonent[1]
    elif command == 'find':
        if abonent[0] in phone_book:
            print(phone_book[abonent[0]])
        else:
            print('not found')
    elif command == 'del':
        if abonent[0] in phone_book:
            del phone_book[abonent[0]]

