#!/usr/bin/python
"""
Возвращает все имена файлов, соответствующие шаблону в дереве каталогов
find() - функция-генератор, использующая функцию-генератор os.walk(),
возвращающая только имена файлов, соответствующие шаблону
Чтобы получить весь список результатов сразу, используется функция findlist()
"""

import fnmatch, os


def find(pattern, startDir=os.curdir):
    for (thisDir, subsHere, filesHere) in os.walk(startDir):
        for name in subsHere + filesHere:
            if fnmatch.fnmatch(name, pattern):
                fullpath = os.path.join(thisDir, name)
                yield fullpath


def findlist(pattern, startDir=os.curdir, doSort=False):
    matches = list(find(pattern, startDir))
    if doSort: matches.sort()
    return matches


if __name__ == '__main__':
    import sys
    # namepattern = '*.py'
    # startDir = r'/mnt/Data/PythonProjects/venv/00_Lutsz/01_start'

    namepattern, startDir = sys.argv[1], sys.argv[2]
    # print(sys.argv)
    for name in find(namepattern, startDir): print(name)
