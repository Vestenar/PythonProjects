"""
отыскивает наибольший файл в формате *.py в дереве каталогов в каталоге стандартной библиотеки
"""

import sys, os, pprint

trace = True
if sys.platform.startswith('win'):
    dirname = r'C:\Users\veste\AppData\Local\Programs\Python\Python37'
else:
    dirname = '/usr/lib/python3.7'

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filesHere)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])