def check_pair(l):
    parnost = 0
    for i in range(len(l)):
        for j in l[i:]:
            if l[i] > j:
                parnost += 1
    return 1 if parnost % 2 == 0 else -1





indata = [int(i) for i in input().split()]
print(check_pair(indata))
