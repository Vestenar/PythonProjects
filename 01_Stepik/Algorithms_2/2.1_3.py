n, m = map(int, input().split())
tables = [None] * n
max_val = 0

# При инициализации у всех таблиц нет родителей и каждая имеет свой размер
for i, x in enumerate(input().split()):
    tables[i] = [int(x), None]
    max_val = max(max_val, int(x))


# Рекурсивная функция поиска корневого родителя с его записью во всех потомков (с целью уменьшения глубины дерева)
def find(i):
    if tables[i][1] is None:
        return i
    tables[i][1] = find(tables[i][1])
    return tables[i][1]


# Поиск родителей и подвешивание одного к другому, если родитель не один и тот же
for _ in range(m):
    dest, src = [find(int(x) - 1) for x in input().split()]
    if dest != src:
        tables[dest][0] += tables[src][0]
        tables[src] = [0, dest]
        max_val = max(max_val, tables[dest][0])
    print(max_val)


