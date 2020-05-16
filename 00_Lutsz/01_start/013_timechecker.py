#!/usr/local/bin/python
import mytimer, sys

print("\n", list(sys.modules.items()))

reps = 10000
repslist = range(reps)


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


def listComp():
    return [abs(x) for x in repslist]


def mapCall():
    return list(map(abs, repslist))


def genExpr():
    return list(abs(x) for x in repslist)


def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)

    return list(gen())


print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytimer.timer(test)
    print('-' * 33)
    print('%-10s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))


def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res


def listComp():
    return [x + 10 for x in repslist]


def mapCall():
    return list(map((lambda x: x + 10), repslist))


def genExpr():
    return list(x + 10 for x in repslist)


def genFunc():
    def gen():
        for x in repslist:
            yield x + 10

    return list(gen())


print("\ncheck same for sum function\n")
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytimer.timer(test)
    print('-' * 33)
    print('%-10s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))