#


def makeset(tree, i):
    tree.append([i + 1, 0])                     # meaning, rank=0


def find(parent, i):
    while i != parent[i][0]:
        i = parent[i][0]
    return i


def union(parent, i, j):                        # checked in video example
    i_id = find(parent, i)
    j_id = find(parent, j)
    if i_id == j_id:
        return
    if parent[i_id][1] > parent[j_id][1]:       # rank i > rank j
        parent[j_id][0] = i_id
    else:
        parent[i_id][0] = j_id
        if parent[i_id][1] == parent[j_id][1]:  # rank i == rank j
            parent[j_id][1] += 1


n, e, d = map(int, input().split())
xes = ['head']

for x in (range(n)):
    makeset(xes, x)

for _ in range(e):
    union(xes, *map(int, input().split()))      # unite all incoming equals

for _ in range(d):
    pass                                        # check diffs in different trees
    x, y = map(int, input().split())
    if find(xes, x) == find(xes, y):
        print(0)
        break
else:
    print(1)

# TODO добавить сжатие путей
