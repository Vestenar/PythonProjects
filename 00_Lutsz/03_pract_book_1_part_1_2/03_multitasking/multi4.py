"""
От класса Process можно породить подкласс, как от класса threading.Thread
объект Queue действует подобно queue.Queue, но обеспечивает обмен между процессами, а не потоками выполнения
"""

import os, time, queue
from multiprocessing import Queue, Process  # общая очередь для процессов (канал + сигналы)


class Counter(Process):
    label = "  @"

    def __init__(self, start, queue):
        self.state = start
        self.post = queue
        # self._popen = None
        # self._closed = False
        # self._parent_pid = os.getpid()
        # self._target = None
        # self._args = tuple()
        # self._kwargs = dict()
        Process.__init__(self)      # для перенаследования имен типа _Х

    def run(self):
        for i in range(3):
            time.sleep(1)
            self.state += 1
            print(self.label, self.pid, self.state)
            self.post.put([self.pid, self.state])

        print(self.label, self.pid, '---')


if __name__ == "__main__":
    print("start", os.getpid())
    expected = 9
    post = Queue()
    p = Counter(0, post)
    q = Counter(100, post)
    r = Counter(1000, post)
    p.start()
    q.start()
    r.start()

    while expected:
        time.sleep(0.5)
        try:
            data = post.get(block=False)
        except queue.Empty:
            print('no data')
        else:
            print('posted', data)
            expected -= 1
    p.join()
    q.join()
    r.join()
    print('finish', os.getpid(), r.exitcode)
quit()
