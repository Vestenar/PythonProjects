import math


def issimple(a):
    r = math.ceil(math.sqrt(a))
    lst = []
    for i in range(3, r):
        if a % i == 0:
            if issimple(i) == []:
                lst.append(i)
                print(lst)
    return lst


r = issimple(600851475143)
print(max(r))
