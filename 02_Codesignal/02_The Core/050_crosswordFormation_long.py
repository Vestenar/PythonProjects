import time
start_time = time.time()
def crosswordFormation(words):
    from itertools import permutations
    ans = 0
    ls = list(permutations(words))
    for ind in range(len(ls)-1,0,-1):
        a,b,c,d = ls[ind]
        if (b,a,d,c) in ls:
            del ls[ind]

    for a in ls:
        print(a)

    for p in ls:

        v1,h1,v2,h2 = p
        for i in range(len(v1)-2):
            for j in range(len(h1)-2):
                if h1[j] in v1 and v1[i] == h1[j] and i < len(v1)-2 and j < len(h1)-2:

                    for k in range(j+2, len(h1)):
                        for l in range(len(v2)):
                            if h1[k]==v2[l]:

                                for m in range(i+2,len(v1)):
                                    for n in range(len(h2)):
                                        if v1[m] == h2[n] and l+(m-i)<len(v2) and n+(k-j)<len(h2):
                                            if v2[l+(m-i)]==h2[n+(k-j)]:
                                                ans+=1

    return ans*2

words = ["aaaaaaaaaaaaaa",
 "baaaaaaaaaaaaa",
 "caaaaaaaaaaaaa",
 "daaaaaaaaaaaaa"]
n = crosswordFormation(words)
print(n)
print("--- %s seconds ---" % (time.time() - start_time))
print('6946368 should be. It\'s', 6946368 == n)