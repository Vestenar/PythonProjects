#!/usr/bin/python
"""
разрезает файл на несколько частей в соответствии с указанным размером
сценарий join.py объединяет эти части в файл
"""

import os, sys
chunksize = int(1024000 * 1.4)


def split(fromfile, todir, chunksize=chunksize):
    if not os.path.exists(todir):
        os.mkdir(todir)                                 # создать каталог, если не существует
    else:
        for name in os.listdir(todir):
            os.remove(os.path.join(todir, name))        # очистить каталог
    partnum = 0
    input = open(fromfile, 'rb')                        # двоичный режим, без декодирования и преобразования
                                                        # символов конца строки
    while True:                                         # eof = прочтена пустая строка
        chunk = input.read(chunksize)
        if not chunk: break
        partnum += 1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()

    input.close()
    assert partnum <=9999                               # сортировка в join невозможна,
    return partnum                                      # если будет 5 цифр


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromfile = input('File to be split: ')
            todir = input('Dir to save parts: ')
            chunksize = int(int(input('Part size in Mb:'))*1024*1024)
        else:
            interactive = False
            fromfile, todir = sys.argv[1:3]
            if len(sys.argv) == 4:
                chunksize = int(sys.argv[-1])
        absfrom, absto = map(os.path.abspath, [fromfile, todir])
        print('Splitting', absfrom, 'to', absto, 'by', chunksize)

        try:
            parts = split(fromfile, todir, chunksize)
        except:
            print('Error during splitting')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Completed!', parts, 'parts in', absto)
        if interactive:
            input('Press any key')