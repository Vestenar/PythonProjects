#!/usr/local/bin/python

print("started:", __name__)


def minimax(test, *args):
    res = args[0]
    for i in args[1:]:
        if test(i, res):
            res = i
    return res


def less(i, res):
    return i < res


def more(i, res):
    return i > res


if __name__ == "__main__":
    print(minimax(less, 5, 6, 2, 3, 5, 7))
    print(minimax(more, 5, 6, 2, 3, 5, 7))
