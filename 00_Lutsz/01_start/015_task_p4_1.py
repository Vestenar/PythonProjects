#!/usr/local/bin/python
import sys
print(sys.version)


def adder(*args):
    out = args[0]
    for i in args[1:]:
        out += i
    print(out)

adder(1,2)
adder("a", "b")
adder(3.14, 2.78)
adder([1,2,3], [4,5,6])

