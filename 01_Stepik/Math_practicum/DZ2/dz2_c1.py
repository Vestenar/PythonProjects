def mimic_dict(string):

    string = string.split()
    d = {'': [string[0]]}
    for i in range(len(string) - 1):
        if string[i] in d:
            if string[i + 1] not in d[string[i]]:
                d[string[i]] += [string[i + 1]]
        else:
            d[string[i]] = [string[i + 1]]
    return d


text = 'Uno dos tres cuatro cinco'
print(mimic_dict(text))
text = '''a cat and a dog
a fly'''
print(mimic_dict(text))
text = '''We are not what we should be
We are not what we need to be
But at least we are not what we used to be
  -- Football Coach'''
print(mimic_dict(text))