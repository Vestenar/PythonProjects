def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    alphabet_dict = dict(enumerate(alphabet))
    for i in range(-1, -len(alphabet), -1):
        encrypted = ''.join([alphabet_dict[(alphabet.index(char) + i) % len(alphabet)] for char in text])
        encrypted = ''
        for char in text:
            index = (alphabet.find(char) + i) % len(alphabet)
            encrypted += alphabet_dict[index]
        print(encrypted)

text = 'BQQMF'
bruteforce(text)
