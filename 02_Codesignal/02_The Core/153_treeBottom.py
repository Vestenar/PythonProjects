import re


def treeBottom(tree):
    pattern = r"(\d+)(?= \(\) \(\))"
    nodes = re.findall(pattern, tree)
    ans = list(map(int, nodes))
    iterat = re.finditer(pattern, tree)
    ind = [m.start(0) for m in iterat]

    tr = []
    for n, i in zip(nodes, ind):
        deep = tree.count("(", 0, i) - tree.count(")", 0, i)
        tr.append(deep)

    return [ans[i] for i in range(len(ans)) if tr[i] == max(tr)]

tree = "(1 () (2 () (3 () (5 () (8 () (13 () (21 () (34 () ()))))))))"
print(treeBottom(tree))
tree = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"
print(treeBottom(tree))
'''
You are given a recursive notation of a binary tree: each node of a tree is represented as a set of three elements:

    value of the node;
    left subtree;
    right subtree.

So, a tree can be written as (value left_subtree right_subtree). It is guaranteed that 1 ≤ value ≤ 109. 
If a node doesn't exist then it is represented as an empty set: (). 
For example, here is a representation of a tree in the given picture:

(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))

Your task is to obtain a list of nodes, that are the most distant from the tree root, in the order from left to right.

In the notation of a node its value and subtrees are separated by exactly one space character.

Example

For

tree = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"

the output should be
treeBottom(tree) = [5, 11, 4].
'''
