def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    text = ''.join(i.upper() for i in text if i.isalpha())
    crypted = ''
    key = str(key)
    for i, char in enumerate(text):
        index = (alphabet.find(char) + int(key[i % len(key)]) * (-1)**(reverse)) % len(alphabet)
        # print(char, index)
        crypted += alphabet[index]
    print(crypted)


text = "У СУДЬИ ЖАРРИКЕСА ПРОНИЦАТЕЛЬНЫЙ УМ"
jarriquez_encryption(text, key=423, alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
text = 'ЧУЦИЮЛКВУФКНЙУГУТССКЩДФИПЮРЯЛЦР'
jarriquez_encryption(text, key=423, alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', reverse=True)

text = 'Some encripted text for this assignment'
jarriquez_encryption(text, key=26101986)