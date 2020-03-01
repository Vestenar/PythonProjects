bin_tree = []
# bin_tree = [(4, 1, 2), (2, 3, 4), (5, -1, -1), (1, -1, -1), (3, -1, -1)]



for i in range(int(input())):
    key, left, right = map(int, input().split())
    bin_tree.append((key, left, right, i))

print(bin_tree)

def in_order(tree, index=0):
    if tree[index][1] != -1:
        in_order(tree, tree[index][1])
    print(tree[index][0], end=' ')
    if tree[index][2] != -1:
        in_order(tree, tree[index][2])

def pre_order(tree, index=0):
    print(tree[index][0], end=' ')
    if tree[index][1] != -1:
        pre_order(tree, tree[index][1])
    if tree[index][2] != -1:
        pre_order(tree, tree[index][2])

def post_order(tree, index=0):
    if tree[index][1] != -1:
        post_order(tree, tree[index][1])
    if tree[index][2] != -1:
        post_order(tree, tree[index][2])
    print(tree[index][0], end=' ')

in_order(bin_tree)
print()
pre_order(bin_tree)
print()
post_order(bin_tree)