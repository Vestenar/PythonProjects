with open('test.txt', 'r') as file:
    data = file.readlines()

with open('test.txt', 'w') as file:
    n = 0
    for line in data:
        line = str(n) + ' ' + line[3:]
        file.write(line)
        n += 1