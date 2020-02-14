def areSimilar1(a, b):
    idx = []
    for i in range(len(a)):
        if a[i] != b[i]:
            idx.append(i)
    if len(idx) == 0:
        return True
    print(a[idx[0]] == b[idx[1]])
    if len(idx) == 2:
        if a[idx[0]] == b[idx[1]] and a[idx[1]] == b[idx[0]]:
            return True
    return False

def areSimilar2(a, b):
    d = [(x, y) for x, y in zip(a, b) if x != y]

    return len(d) == 0 or (len(d) == 2 and d[0][::-1] == d[1])



a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
print(areSimilar(a, b))