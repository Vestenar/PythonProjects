'''
# анонимные каналы и потоки выполнения вместо процессов;
# эта версия работает и в Windows
'''

import os, time, threading


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz/4)
        msg = ('Сообщение %d' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent(pipein):
    while True:
        line = os.read(pipein, 32).decode()
        print('Parent %d got[%s] at % s' % (os.getpid(), line, time.strftime('%Y-%b-%d %H:%M:%S')))

pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)
