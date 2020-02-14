def check_pair(l):
    parnost = 0
    for i in range(len(l)):
        for j in l[i:]:
            if l[i] > j:
                parnost += 1
    return parnost



m, n = map(int, input().split())
indata = []
for k in range(m):
    indata += [int(i) for i in input().split()]
print(indata)
base_l = list(range(n*m))[1:]
base_lo = []
for i in range(m):
    base_lo += base_l[i * n:(i + 1) * n][::(-1)**i]
    print(base_lo)
print('Бинго!' if check_pair(indata) % 2 == check_pair(base_lo) % 2 else 'Не повезло...')