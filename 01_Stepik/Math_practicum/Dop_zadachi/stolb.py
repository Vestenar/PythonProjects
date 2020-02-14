smm = int(input())

def find(smm):
    for i in range(1000):
        if sum(map(int, list(str(i)))) != smm:
            continue
        for j in range(i, 0, -1):
            print(j, '->>', i - j)
            if sum(map(int, list(str(j)))) + sum(map(int, list(str(i - j)))) != smm:
                break
        print(i)
        return i

print(find(smm))
