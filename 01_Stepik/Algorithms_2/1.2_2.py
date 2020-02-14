def leveling(tree):  #  рекурсивный обход

    depth = [-1 for _ in range(len(tree))] + [0]

    def count(ind):
        if depth[ind] == -1:
            depth[ind] = count(tree[ind]) + 1
        return depth[ind]

    # print(list(count(ind) for ind in range(len(tree))))
    # print(depth)
    return max(count(ind) for ind in range(len(tree)))


def traverse_tree_stack(tree, root):        # эмуляция рекурсии через стек
    stack = []
    stack.append((root, 0))
    depth = 1
    while len(stack):
        depth = max(depth, len(stack))
        current = stack.pop()
        children = tree.get(current[0], [])
        if current[1] + 1 > len(children):
            continue
        stack.append((current[0], current[1] + 1))
        stack.append((children[current[1]], 0))
    return depth


def main():
    n = int(input())
    tree = [int(leaf) for leaf in input().split()]
    # print(leveling(tree))

    tree_dict = {}
    for index, parent in enumerate(tree):
        kids = tree_dict.get(parent, [])
        kids.append(index)
        tree_dict[parent] = kids

    print(tree_dict)

    root = tree_dict[-1][0]
    print(traverse_tree_stack(tree_dict, root))


# def test():
#     assert leveling([9, 7, 5, 5, 2, 9, 9, 9, 2, -1]) == 4
#     # assert leveling(1, [4, -1, 4, 1, 1]) == 3
#     # assert leveling(0, [-1, 0, 4, 0, 3]) == 4


if __name__ == '__main__':
    main()
    # test()

# def tree_height_bottom_up(parents):
#     """Time complexity: O(n), where n = len(parents)"""
#     depths = [-1] * (len(parents)) + [0]
#
#     def count_depth(i):
#         if depths[i] == -1:
#             depths[i] = count_depth(parents[i]) + 1
#         return depths[i]
#
#     return max(count_depth(i) for i in range(len(parents)))
#
#
# def main():
#     n_ = input()
#     parents = [int(i) for i in input().split()]
#
#     print(tree_height_bottom_up(parents))
#
#
# def test():
#     assert tree_height_bottom_up([9, 7, 5, 5, 2, 9, 9, 9, 2, -1]) == 4
#     assert tree_height_bottom_up([4, -1, 4, 1, 1]) == 3
#     assert tree_height_bottom_up([-1, 0, 4, 0, 3]) == 4
#
# if __name__ == '__main__':
#     test()


