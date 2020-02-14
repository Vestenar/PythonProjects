def whoseTurn(p):
    ks = p.split(";")
    w = (ord(ks[0][0]) + int(ks[0][1]) + ord(ks[1][0]) + int(ks[1][1])) % 2
    b = (ord(ks[2][0]) + int(ks[2][1]) + ord(ks[3][0]) + int(ks[3][1])) % 2
    return w == b


p = "b1;g1;b8;g8"
print(whoseTurn(p))

'''
Imagine a standard chess board with only two white and two black knights placed 
in their standard starting positions: the white knights on b1 and g1; the black knights on b8 and g8.

There are two players: one plays for white, the other for black. During each move, 
the player picks one of his knights and moves it to an unoccupied square according 
to standard chess rules. Thus, a knight on d5 can move to any of the following squares: 
b6, c7, e7, f6, f4, e3, c3, and b4, as long as it is not occupied by either a friendly 
or an enemy knight.

The players take turns in making moves, starting with the white player. 
Given the configuration p of the knights after an unspecified number of moves, 
determine whose turn it is.
'''
