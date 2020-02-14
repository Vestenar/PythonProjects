def myreduce(function, sequence):
    tally = sequence[0]

    for next in sequence[1:]:
        tally = function(tally, next)
    return tally


print(myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))
print(myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5]))
