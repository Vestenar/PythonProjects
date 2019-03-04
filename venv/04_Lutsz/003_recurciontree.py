def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
           tot += x
        else:
            tot += sumtree(x)

    return tot



# s = [1,[2,[3,4],5],6]
# print(sumtree(s))
print(sumtree([1, [2, [3, [4, [5]]]]])) # Выведет 15 (центр тяжести справа)
print(sumtree([[[[[1], 2], 3], 4], 5])) # Выведет 15 (центр тяжести слева)