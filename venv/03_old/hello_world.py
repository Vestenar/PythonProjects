'''def sum(param1, param2):
    return param1 + param2            # return result to the function caller

param1 = int(input())
param2 = int(input())
c = sum(param1, param2)
print(c)

nlen=0
def checkPalindrome(inputString):
    nlen = len(inputString)
    if nlen == 1:
        t = True
    else:
        for i in range(nlen//2):
            if inputString[i] == inputString[-i-1]:
                t = True
            else:
                t = False
                break
    return t

inputString = "sasass"
print(checkPalindrome(inputString))'''


'''def adjacentElementsProduct(inputArray):
    test = inputArray[0]*inputArray[1]
    for i in range((len(inputArray)-2)):
            nmax = inputArray[i+1]*inputArray[i+2]
            if test < nmax:
                test = nmax
    return test


inputArray = [6, 2, 3, 8]
max = 0
max = adjacentElementsProduct(inputArray)
print(max)'''

'''sequence = [1, 3, 2, 1]

count = 0
t = True
t1 = True
t2 = True

narray = list(sequence)
for b in range(2):
    for i in range(len(narray)-1):
            if narray[i] < narray[i-1]:
                narray[i-1:i] = []
                count += 1
if count < 2:
    t1 = False


count = 0
narray2 = list(sequence)

narray = list(sequence)
for b in range(2):
    for i in range(len(narray)-1):
            if narray[i] < narray[i-1]:
                narray[i:i+1] = []
                count += 1
if count < 2:
    t1 = False

t = t1 or t2

print(narray)
print(narray2)
print(t1, t2, t)'''
'''t = True
count = 0
for i in range(len(sequence)):
    if count > 2:
        data = False
        break
    if i+1 < len(sequence) and sequence[i] >= sequence[i+1]:
        count += 1
    if i+2 < len(sequence) and sequence[i] >= sequence[i+2]:
        count += 1

print(t)
'''
'''matrix = [[1,1,1],
 [2,2,2],
 [3,3,3]]
price = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i != 0 and matrix[i-1][j] == 0:
            matrix[i][j] = 0



for row in matrix:
    for elem in row:
        price += elem
print(price)'''

'''inputArray = ["aba", "aa", "ad", "vcd", "aba"]

lenw = 0
out = []

for i in range(len(inputArray)):
    if lenw < len(inputArray[i]):
        lenw = len(inputArray[i])

for i in range(len(inputArray)):
    if len(inputArray[i]) == max(len(s) for s in inputArray):
        out.append(inputArray[i])

print(out)'''

'''s1 = "aabzca"
s2 = "adcaaz"
n = 0
for i in s1:
    if i in s2:
        n +=1
        s2 = s2.replace(i, "0", 1)

print(n)'''

'''n = str(int(123610))
mid = len(n)//2
n1 = n[:mid]
n2 = n[mid:]
sum1 = 0
for i in range(len(n1)):
    sum1 +=int(n1[i])
for i in range(len(n2)):
    sum1 -=int(n2[i])

if sum1 == 0:
    out = "Счастливый"
else:
    out = "Обычный"
print(out)'''

'''s = 'aaaabbcccaabb'
t = s[0]
count = 0
out = ''
for i in s:
    if i == t:
        count += 1
    else:
        out = out + t+str(count)
        t = i
        count = 1
out = out + t + str(count)

print(t, out)'''

'''a = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
print([1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77])
m = max(a)

for i in range(1, len(a)):
    if a[-i] != -1:
        a[-i], a[a.index(m)] = a[a.index(m)], a[-i]
        m = max(a[:-i])
print(a)
'''

'''s = "The ((quick (brown) (fox) jumps over the lazy) dog)"
count = s.count('(')
op = []
cl = []
id = 0
for ch in s:
    if ch == '(':
        op.append(id)
    id += 1
op = op[::-1]

id = 0
'ускорить поиск скобок путем определения начала поиска'
for i in range(count):
    for ch in s:
        if ch == ')' and id > op[i] and id not in cl:
            cl.append(id)
            break
        id += 1
    id = 0

for i in range(count):
    sh = s[op[i]+1:cl[i]]
    s = s.replace(sh, sh[::-1])

s = s.replace("(", "")
s = s.replace(")", "")
print(s)'''

'''s = "The ((quick (brown) (fox) jumps over the lazy) dog)"
while ')' in s:
    j = s.index(')')
    i = s.rindex('(', 0, j)
    s = s[:i] + s[j-1:i:-1] + s[j+1:]
print(s)'''

'''a = [50]
b = [0,0]
for i in range(len(a)):
    b[i%2] += a[i]
print(b)'''

'''
a = ["*****",
 "*abc*",
 "*ded*",
 "*****"]
picture = ["abc", "ded"]
picture.insert(0,"*" * len(picture[0]))
picture.append("*" * len(picture[0]))
for i in range(len(picture)):
    test = picture[i]
    test = "*" + test + "*"
    picture[i] = test
print(picture)'''



'''def areSimilar(a, b):
    idx = []
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            idx.append(i)
    if len(idx) == 0:
        return True
    if len(idx) != 2:
        return False
    if a[idx[0]] == b[idx[1]] and a[idx[1]] == b[idx[0]]:
        return True
    else:
        return False
'заносим в массив idx только те символы, которые не совпадают в исходных массивах, если таких символов только две пары, то проверяем взаимозаменяемость пар'


a = [1, 2, 2]
b = [2, 1, 1]
print(areSimilar(a, b))'''

'''def arrayChange(inputArray):
    n = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            n += inputArray[i - 1] - inputArray[i] + 1
            inputArray[i] += inputArray[i-1] - inputArray[i] +1


    return n
inputArray = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
print(arrayChange(inputArray))
'''


'''a = [int(i) for i in input().split()]
b = []
ans = ''
for i in range(len(a)):
    if a.count(a[i]) > 1 and (a[i] not in b):
        b.append(a[i])

for i in b:
    ans += str(i) + ' '

print(ans)
'''

'''
проверка строки на возможность получить палиндром перестановкой символов.
считаем только символы, количество которых нечетное и заносим в массив
def palindromeRearranging(inputString):
    a = []
    for i in range(len(inputString)):
        if inputString.count(inputString[i]) % 2 != 0:
            if inputString[i] != inputString[i-1]:
                a.append(inputString.count(inputString[i]))
    return len(a) <= 1

task = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccc'
print(palindromeRearranging(task))
'''

'''САПЕР codesignal
def minesweeper(matrix):
    row, col = len(matrix), len(matrix[0])
    ans = [[0 for c in range(col)] for r in range(row)]

    for i in range(row):
        for j in range(col):
            if matrix[i][j]:
                ans[i][j] = -1
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < row and 0 <= aj < col and matrix[ai][aj]:
                        ans[i][j] += 1
    return ans


task = [[True,False,False],[False,True,False],[False,False,False]]
print(minesweeper(task))
'''

''' 
def avoidObstacles(inputArray):
    jump = 1
    a = 0
    while a < max(inputArray)//jump:
        jump += 1
        for i in range(1, max(inputArray)//jump+1):
            if jump*i not in inputArray:
                a += 1
            else:
                a = 0
                break

    return jump


task = [5, 3, 6, 7, 9]
print(avoidObstacles(task))
'''


''' # эффект блюр для "фотографии"
def boxBlur(image):
    row, col = len(image), len(image[0])  # row rows, col columns
    ans = []
    for i in range(1, row-1):
        ans.append([])
        for j in range(1, col-1):
            flsum = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    flsum += image[i+k][j+l]
            ans[i-1].append(int(flsum/9))

    return ans


task = [[7, 4, 0, 1], [5, 6, 2, 2], [6, 10, 7, 8], [1, 4, 2, 0]]
print(boxBlur(task))
'''








'''codesignal является ли имя переменой корректным
def variableName(name):
    if not name[0].isalpha() and name[0] != '_':
        return False
    else:
        for i in range(1, len(name)):
            if not name[i].isalnum() and name[i] != '_':
                return False

    return True

name = 'var1_'
print(variableName(name))

'''







'''codesignal
def absoluteValuesSumMinimization(a):
    # x = a[0]
    list = {}

    for i in range(len(a)):
        sabs = 0
        for j in range(len(a)):
            sabs += abs(a[j] - a[-(i+1)])
        list[sabs] = a[-(i+1)]

    print(list)
    return list[min(list)]


test = [1, 1, 3, 4]
print(absoluteValuesSumMinimization(test))

'''

''' задача на брутфорс всех перестановок
def stringsRearrangement(inputArray):
    import itertools
    perm = list(itertools.permutations(inputArray, len(inputArray))) #полный список всех перестановок
    for k in perm: #проверяем каждый вариант перестановки
        for i in range(1, len(k)):
            a = k[i]
            b = k[i-1]
            count = 0
            for index in range(len(a)):
                if a[index] != b[index]:
                    count += 1
            if count != 1:
                break
        if count == 1:
            return True
    return False'''

'''#codesignal
#Given array of integers, find the maximal possible sum of some of its k consecutive elements.

def arrayMaxConsecutiveSum(a, k):
    c = m = sum(a[:k]) #посчитали исходную сумму

    for i in range(len(a) - k):
        c = c + a[i + k] - a[i] #уменьшили сумму на предыдущий элемент и увеличили на следующий
        m = max(c, m) #проверили максимум и сохранили в m

    return m


test = [1, 3, 2, 4]
k = 3
print(arrayMaxConsecutiveSum(test, k))'''