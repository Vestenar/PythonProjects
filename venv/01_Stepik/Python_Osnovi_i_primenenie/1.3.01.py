def list_sum(lst):
    result = 0
    for el in lst:
        result += el
    return result

def sum(a, b):
    return a+b

y = sum(14,29)
z = list_sum([1,2,3])
print(y)
print(z)

a = []
print(a.append('test'))
print(id(a))

#СТЕК
a = [1,2,3]
a.append(4)
a.append(5)
print(a)

top = a.pop()
print(top)
print(a)

print(a.pop())
print(a)
