import os
from multiprocessing import Process, Pipe
""" реализует взаимодействие между процессами посредством анонимных каналов
    Объекты передаются в один конец канала connections и принимаются из другого конца"""


def sender(pipe):
    """передает процесс родителю через анонимный канал"""
    pipe.send(['spam'] + [42, 'eggs'])
    pipe.close()

def talker(pipe):
    """передает и принимает объекты из канала"""
    pipe.send(dict(name="Bob", spam=42))
    reply=pipe.recv()
    print('talker got:', reply)

if __name__ == '__main__':
    (parentEnd, childEnd) = Pipe()
    Process(target=sender, args=(childEnd,)).start()
    print('Parent got:', parentEnd.recv())
    parentEnd.close()

    (parentEnd, childEnd) = Pipe()
    child = Process(target=talker, args=(childEnd,))
    child.start()
    print('Parent got:', parentEnd.recv())
    parentEnd.send({x * 2 for x in 'spam'})
    child.join()
    print('parent exit')
