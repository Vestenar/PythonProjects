functs = {
    "one": lambda x: print(x),
    "two": lambda x: print(x*2),
    "three": lambda x: print(x*3)
    }

key = "one"
f = functs[key]
f(123)
key = "two"
h = functs[key]
h(22)
g = functs["three"]("123-")