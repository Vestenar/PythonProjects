def bishopDiagonal(bishop1, bishop2):
    cell = '.abcdefgh'
    c1,s1 = cell.index(bishop1[0]),int(bishop1[1])
    c2,s2 = cell.index(bishop2[0]),int(bishop2[1])
    if abs(c1-c2) == abs(s1-s2):
        print((c1,s1), "...", (c2,s2))
        if c1+s1 == c2+s2:
            r = min(8-c1, s1-1)
            l = min(c2-1, 8-s2)
            print('u-l', r, l)
            c1 += r
            s1 -= r
            c2 -= l
            s2 += l
            print((c1, s1), "...", (c2, s2))
            bishop1 = "".join([cell[c1],str(s1)])
            bishop2 = "".join([cell[c2],str(s2)])
        else:
            r = min(8-c1, 8-s1)
            l = min(c2-1, s2-1)
            print('l-u', r, l)
            c1 += r
            s1 += r
            c2 -= l
            s2 -= l
            bishop1 = "".join([cell[c1], str(s1)])
            bishop2 = "".join([cell[c2], str(s2)])
    else: return sorted([bishop1, bishop2])
    return sorted([bishop1, bishop2])




bishop1 = "d5"
bishop2 = "f7"
print(bishopDiagonal(bishop1,bishop2))

# bishop1 = "b5"
# bishop2 = "d8"
# print(bishopDiagonal(bishop1,bishop2))

'''In the Land Of Chess, bishops don't really like each other. 
In fact, when two bishops happen to stand on the same diagonal, 
they immediately rush towards the opposite ends of that same diagonal.

Given the initial positions (in chess notation) of two bishops, 
bishop1 and bishop2, calculate their future positions. 
Keep in mind that bishops won't move unless they see each other along the same diagonal.

Example

    For bishop1 = "d7" and bishop2 = "f5", the output should be
    bishopDiagonal(bishop1, bishop2) = ["c8", "h3"].

    For bishop1 = "d8" and bishop2 = "b5", the output should be
    bishopDiagonal(bishop1, bishop2) = ["b5", "d8"].

    The bishops don't belong to the same diagonal, so they don't move.
    '''
