def myzip(*args):
    iters = map(iter, args)
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)

print(list(myzip("abc", "lmnop")))
# works in 2.6 only