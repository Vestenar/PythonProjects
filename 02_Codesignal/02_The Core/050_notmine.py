import time
start_time = time.time()
def crosswordFormation(words):
    from itertools import permutations as perms
    from collections import defaultdict as ddic
    ans = 0
    for p in perms(words):
        M = ddic(int)
        a,b,c,d = p
        for i in range(2, min(len(a),len(b))):
            for p in range(len(a) - i):
                for q in range(len(b) - i):
                    M[a[p],a[p+i],b[q],b[q+i]] += 1
        print(dict(M))
        for i in range(2, min(len(c),len(d))):
            for p in range(len(c) - i):
                for q in range(len(d) - i):
                    ans += M[c[p],d[q],c[p+i],d[q+i]]
    return ans


def crosswordFormation(words):
    from itertools import permutations as p
    c = 0
    for l in p(words):
        for d1 in range(len(l[0])-2):
            s1 = [i for i,j in enumerate(l[1]) if j == l[0][d1]]
            print("s1",s1)
            for d2 in range(d1+2, len(l[0])):
                s2 = [i for i,j in enumerate(l[2]) if j == l[0][d2]]
                print("s2",s2)
                for cw1 in s1:
                    for cw2 in s2:
                        for c1, c2 in zip(l[1][cw1+2:],l[2][cw2+2:]):
                            for c3, c4 in zip(l[3],l[3][d2-d1:]):
                                c += c1 == c3 and c2 == c4
    return c

words = ["phenomenon",
 "remuneration",
 "particularly",
 "pronunciation"]
n = crosswordFormation(words)
print(n)
print("--- %s seconds ---" % (time.time() - start_time))
print('6946368 should be', 6946368 == n)