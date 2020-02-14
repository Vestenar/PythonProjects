import random as rd
clear_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 6
rd.seed(42)


def disc_generator(alphabet):
    alphabet = list(alphabet)
    rd.shuffle(alphabet)
    alphabet = "".join(alphabet)
    return alphabet


discs = [disc_generator(clear_alphabet) for _ in range(n)]


def caesar(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    alphabet_dict = dict(enumerate(alphabet))
    crypted = ''.join([alphabet_dict[(alphabet.index(i) + key) % len(alphabet)] for i in text])
    return crypted


def jefferson_encryption(text, discs, step, reverse=False):
    crypt = ''
    if reverse: step *= -1
    text = text.upper().replace('.','').replace(',','').replace(' ','')
    for char in range(len(text)):
        if text[char] in discs[0]:
            crypt += caesar(text[char], step, discs[char % n])
    return crypt


text = 'SOMEENCRIPTEDTEXT'
step = 13
print(jefferson_encryption(text, discs, step))
text = 'DSZNNXZCBOSASGTAS'
print(jefferson_encryption(text, discs, step, True))


clear_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
n = 36
rd.seed(42)
discs = [disc_generator(clear_alphabet) for _ in range(n)]
text = 'Съешь еще этих мягких французских булок. Кстати, в этом тексте пришлось заменить одну букву...'
step = 4
print(jefferson_encryption(text, discs, step))
text = 'ДЮИЖЖНККЩЖТЮШМЦНЩЦДЕМХННОЭЛАПОВЖМЯЬБГЙПМЩХАВЫЖВНМСНЯВНЮДХЖГЖГХФЫСДХЯЖЕСТЬЗШШ'
print(jefferson_encryption(text, discs, step, True))
