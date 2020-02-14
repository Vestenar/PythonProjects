'''
использование мьютексов в родительском/главном потоке выполнения для определения
момента завершения дочерних потоков, взамен time.sleep; блокирует stdout, чтобы
избежать конфликтов при выводе;
'''

import _thread as thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]

def counter(myID, count):
    for i in range(count):
        stdoutmutex.acquire()  # блокирует stdout для текущего потока
        print('[%s] => %s' % (myID, i))
        stdoutmutex.release()
    exitmutexes[myID].acquire()  # сигнал главному потоку

for i in range(10):
    thread.start_new_thread(counter, (i, 10))

for mutex in exitmutexes:
    while not mutex.locked():
        pass
print('Main thread exited')

