from xml.etree import ElementTree

colors = {'red': 0, 'green': 0, 'blue': 0}
# str_colors = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
str_colors = input()
with open('cubes.xml', 'w') as file:
    file.write(str_colors)

tree = ElementTree.parse('cubes.xml')

root = tree.getroot()
# print(tree, root.tag, '\n', root.attrib)


def counter(root, level):
    # print(root.tag, root.attrib, level)
    colors[root.attrib['color']] += level
    level += 1
    for cube in root:
        # print('______', root.tag, root.attrib, level)
        counter(cube, level)


level = 1
counter(root, level)
print(' '.join(map(str, [colors[index] for index in ('red', 'green', 'blue')])))
