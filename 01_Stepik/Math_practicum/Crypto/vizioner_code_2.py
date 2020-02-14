def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    text = ''.join(i.upper() for i in text if i.isalpha())
    crypted = ''
    if key % 100000 == 0:
        print(key)
    key = str(key)
    for i, char in enumerate(text):
        index = (alphabet.find(char) + int(key[i % len(key)]) * (-1)**(reverse)) % len(alphabet)
        crypted += alphabet[index]

    if 'ДАКОСТА' in crypted:
        print(crypted)
        print(key)
        return True



text = '''ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖОИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС'''

# alphabet = str(sorted(set(text)))
alphabet1 = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

for k in range(200000, 999999):
    if jarriquez_encryption(text, k, alphabet1, reverse=True):
        break
