"""Реализует взаимодействие с помощью объектов разделяемой памяти из пакета
В Windows передаваемые объекты используются совместно, а глобальные - нет
Последняя проверка отражает наиболее типичный случай использования:
распределение заданий между процессами
"""

import os
from multiprocessing import Process, Value, Array

procs = 3                   # глобальные переменные, отдельные для каждого процесса
count = 0                   # не являются совместно используемыми

def showdata(label, val, arr):
    """
    выводит значения дынных в этом процессе
    """
    msg = '%-12s: pid:%4s, global:%s, value:%s, array:%s'
    print(msg % (label, os.getpid(), count, val.value, list(arr)))

def updater(val, arr):
    """
    обменивается данными через разделяемую память
    """
    global count
    count += 1
    val.value += 1
    for i in range(procs): arr[i] += 1

if __name__ == "__main__":
    scalar = Value('i', 0)      # разделяемая память: предусматривает синхронизацию потоков
    vector = Array('d', procs)  # коды типов из ctype: int, double

    # вывести начальные значения в родительском процессе
    showdata('parent start', scalar, vector)

    # породить дочерний процесс, передать данные в разделяемой памяти
    p = Process(target=showdata, args=('child', scalar, vector))
    p.start(); p.join()

    # изменить данные в родителе и передать через разделяемую память
    # ждать завершения каждого потомка
    # все потомки видят изменения, выполненные в родительском процессе
    # и переданные в виде аргументов (не в глобальной памяти)

    print('\nlooop1 (обновление в родителе, последовательные потомки)')
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s' % i), scalar, vector))
        p.start(); p.join()

    # то же самое, но потомки запускаются параллельно
    # все они видят результат последней итерации
    # потому что хранятся в совместно используемых объектах

    print('\nlooop2 (обновление в родителе, параллельные потомки)')
    ps = []
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s' % i), scalar, vector))
        p.start()
        ps.append(p)
    for p in ps: p.join()

    # объекты в разделяемой памяти изменяются потомками
    # ждать завершения каждого из них

    print('\nlooop3 (обновление в последовательных потомках)')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start(); p.join()
        showdata('parent temp', scalar, vector)

    # то же самое, но потомки запускаются параллельно

    print('\nlooop4 (обновление в последовательных потомках)')
    ps = []
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)
    for p in ps: p.join()

    showdata('parent end', scalar, vector)