'''
экземпляры класса Thread, сохраняющие информацию о состоянии и обладающие
методом run() для запуска потоков выполнения; в реализации используется
высокоуровневый и Java-подобный метод join класса Thread модуля threading
(вместо мьютексов и глобальных переменных), чтобы известить главный родительский
поток о завершении дочерних потоков
'''

import threading

class MyThread(threading.Thread):
    def __init__(self, myID, count, mutex):
        self.myID = myID
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:                    # синхронизация доступа к stdout
                print('[%s] => %s ' % (self.myID, i))

stdoutmutex = threading.Lock()
threads = []
for i in range(10):
    thread = MyThread(i, 100, stdoutmutex)
    thread.start()                             # вызвать метод run()
    threads.append(thread)

for thread in threads:
    thread.join()                              # ждать завершения потока
print('Main thread exited')
