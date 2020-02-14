import random as rd

def print_mimic(mimic_dict, word):
    import random as rd
    out_text = [word]
    for i in range(200):
        n = rd.choice(mimic_dict[word])
        out_text.append(n)
        if n not in mimic_dict:
            n = ''
        word = n
    return ' '.join(out_text)


mimic = {'': ['We'], 'We': ['are'], 'are': ['not'], 'not': ['what'], 'what': ['we'], 'we': ['should', 'need', 'are', 'used'], 'should': ['be'], 'be': ['We', 'But', '--'], 'need': ['to'], 'to': ['be'], 'But': ['at'], 'at': ['least'], 'least': ['we'], 'used': ['to'], '--': ['Football'], 'Football': ['Coach']}
word = ''
print(print_mimic(mimic, word))
