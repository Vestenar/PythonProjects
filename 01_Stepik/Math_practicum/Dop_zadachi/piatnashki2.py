
def check_pair(l):
    parnost = 0
    for i in range(len(l)):
        for j in l[i:]:
            if l[i] > j:
                parnost += 1
    return parnost



indata = []
for n in range(4):
    indata += [int(i) for i in input().split()][::-1**n%2]
base_l = list(range(16))[1:]
print('Бинго!' if check_pair(indata) % 2 == check_pair(base_l) % 2 else 'Не повезло...')