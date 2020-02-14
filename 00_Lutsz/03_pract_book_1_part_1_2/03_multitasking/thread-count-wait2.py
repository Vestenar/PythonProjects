'''
использование простых глобальных данных (не мьютексов) для определения момента
завершения всех потоков в родительском/главном потоке; потоки совместно
используют список, но не его элементы, при этом предполагается, что после
создания список не будет перемещаться в памяти
'''

import _thread as thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [False]*10

def counter(myID, count):
    for i in range(count):
        stdoutmutex.acquire()  # блокирует stdout для текущего потока
        print('[%s] => %s' % (myID, i))
        stdoutmutex.release()
    exitmutexes[myID] = True  # сигнал главному потоку

for i in range(10):
    thread.start_new_thread(counter, (i, 100))

while False in exitmutexes:
    pass

print('Main thread exited')
