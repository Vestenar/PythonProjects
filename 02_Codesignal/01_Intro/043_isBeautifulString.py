def isBeautifulString(inputString):
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    n = inputString.count(alphabet[0])
    for i in alphabet:
        if inputString.count(i) > n:
            return False
        n = inputString.count(i)
    return True



#реализация через сравнение массивов и метод string, в котором содержится константа
# import string
# def isBeautifulString(s):
#     l = [s.count(i) for i in string.ascii_lowercase[::-1]]
#     return l == sorted(l)

#реализация метода через map
# def isBeautifulString(inputString):
#
#     counts = list(map(inputString.count, 'abcdefghijklmnopqrstuvwxyz')) #создает массив количества вхождений
#     print(counts)
#     return all(x >=y for x, y in zip(counts, counts[1:]))
task = "abcdefghijklmnopqrstuvwxyz"
print(isBeautifulString(task))




'''
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

    For inputString = "bbbaacdafe", the output should be
    isBeautifulString(inputString) = true;
    For inputString = "aabbb", the output should be
    isBeautifulString(inputString) = false;
    For inputString = "bbc", the output should be
    isBeautifulString(inputString) = false.
'''