with open('dataset_48784_9.txt', 'r') as f:
    numoflines = 0
    letters = []
    for line in f:
        numoflines += 1
        letters.append(line[0])

print(numoflines)
print(' '.join(letters))