from PIL import Image
from rcviz import CallGraph, viz

cg = CallGraph(filename="fibo.png")
@viz(cg)
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n-1) + fib1(n-2)

fib1 = viz(fib1)

# Image.open('./fibo.png').show()
