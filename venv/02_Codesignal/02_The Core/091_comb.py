def combs(comb1, comb2):
    len1 = len(comb1)
    len2 = len(comb2)
    comb1 = int(comb1.replace("*", "1").replace(".","0"),2)
    comb2 = int(comb2.replace("*", "1").replace(".","0"),2)
    print(comb1, comb2)
    answer = len1 + len2
    for i in range(-len1, len2 + 1):
        if i < 0:
            tmp = comb2 << (-i) & comb1
            length = max(-i + len2, len1)
        else:
            tmp = comb1 << i & comb2
            length = max(i + len1, len2)
        if tmp == 0 and answer > length:
            answer = length
    return answer


comb1 = "*..*"
comb2 = "*.*"

print(combs(comb1,comb2))

'''
Miss X has only two combs in her possession, both of which are old and miss a tooth or two. 
She also has many purses of different length, in which she carries the combs. 
The only way they fit is horizontally and without overlapping. Given teeth' positions on both combs, 
find the minimum length of the purse she needs to take them with her.

It is guaranteed that there is at least one tooth at each end of the comb.
It is also guaranteed that the total length of two strings is smaller than 32.
Note, that the combs can not be rotated/reversed.

Example

For comb1 = "*..*" and comb2 = "*.*", the output should be
combs(comb1, comb2) = 5.

Although it is possible to place the combs like on the first picture, the best way to do this is either picture 2 or picture 3.
'''
