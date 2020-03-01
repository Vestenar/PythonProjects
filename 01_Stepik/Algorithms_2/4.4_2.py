bin_tree = []
# bin_tree = [(4, 1, 2, 0), (2, 3, 4, 1), (6, 5, 6, 2), (1, -1, -1, 3), (3, -1, -1, 4), (5, -1, -1, 5), (7, -1, -1, 6)]



for i in range(int(input())):
    key, left, right = map(int, input().split())
    bin_tree.append((key, left, right, i))

print(bin_tree)

def check_tree(tree):
    check_list = []
    def in_order(tree, index=0):
        nonlocal check_list
        if tree[index][1] != -1:
            in_order(tree, tree[index][1])
        check_list.append(tree[index][0])
        if tree[index][2] != -1:
            in_order(tree, tree[index][2])
    in_order(tree)
    if check_list == sorted(check_list):
        return True
    else:
        return False

print('CORRECT' if check_tree(bin_tree) else 'INCORECT')
