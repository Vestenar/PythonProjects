def caesar(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    import string
    alphabet_dict = dict(enumerate(alphabet))

    text = ''.join(i.upper() for i in text if i.isalnum())
    crypted = ''.join([alphabet_dict[(alphabet.index(i) + key) % len(alphabet)] for i in text])
    print('Encrypted: ', crypted)
    print('Decrypted back: ', text)



text = 'А с русским текстом выйдет?'
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = 1

caesar(text, key, alphabet)
