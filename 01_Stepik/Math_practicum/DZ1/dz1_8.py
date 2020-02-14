words = ['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']
first = sorted(list(filter(lambda x: len(x) > 0 and x[0] == 'x', set(words))))
rest = sorted(list(filter(lambda x: x not in first, words)))
print(first)
print(rest)