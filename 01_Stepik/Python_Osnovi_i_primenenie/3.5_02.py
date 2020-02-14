import json, pprint

sample = '[{"name": "G", "parents": ["F"]}, '\
         '{"name": "A", "parents": []}, '\
         '{"name": "B", "parents": ["A"]}, '\
         '{"name": "C", "parents": ["A"]}, '\
         '{"name": "D", "parents": ["B", "C"]}, '\
         '{"name": "E", "parents": ["D"]}, ' \
         '{"name": "F", "parents": ["D"]}, ' \
         '{"name": "X", "parents": []}, ' \
         '{"name": "Y", "parents": ["X", "A"]}, ' \
         '{"name": "Z", "parents": ["X"]}, ' \
         '{"name": "V", "parents": ["Z", "Y"]}, ' \
         '{"name": "W", "parents": ["V"]}]'

massive = json.loads(sample)
count = {cls["name"]: 1 for cls in massive}
# print(massive)


parents = {}
for cls in count:
    deti = []
    for mas in massive:
        if cls in mas["parents"]: deti.append(mas["name"])
    parents[cls] = deti

# pprint.pprint(parents)


def check_kids(parent, kids, grand):

    for kid in kids:
        if kid not in visited:
            count[grand] += 1
            # print(kid, ' => ', parents[kid], f'{grand=}, {visited=}', count[grand])
            visited.append(kid)
            check_kids(kid, parents[kid], grand)



for cls in (parents):
    visited = []
    check_kids(cls, parents[cls], cls)


for cls in sorted(count):
    print(f"{cls} : {count[cls]}")