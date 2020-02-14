'''
основы анонимных каналов
дескрипторы файлов с входным и выходным концами
'''

import os, time


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Message %03d' % zzz).encode()  # канал - двоичный файл
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent():
    pipein, pipeout = os.pipe()  # создается канал с двумя концами
    if os.fork() == 0:  # создается копия процесса
        # os.close(pipein)
        child(pipeout)  # в копии вызывается child()
    else:
        # os.close(pipeout)
        # pipein = os.fdopen(pipein)
        while True:  # в родителе слушается канал
            line = os.read(pipein, 16).decode()  # остановиться до получения не более 16 байт в канале
            # line = pipein.readline()[:-1]
            print('Parent %d got[%s] at % s' % (os.getpid(), line, time.strftime('%Y-%b-%d %H:%M:%S')))


parent()
