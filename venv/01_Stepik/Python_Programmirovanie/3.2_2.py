'''
Когда Антон прочитал «Войну и мир», ему стало интересно,
сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы,
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Sample Input 1:

a aa abC aa ac abc bcd a

Sample Output 1:

ac 1
a 2
abc 2
bcd 1
aa 2
'''

a = input().lower().split()
dict = {}
for i in a:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
for key, value in dict.items():
    print(key, value)