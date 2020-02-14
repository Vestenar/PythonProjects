def chessKnight(cell):
    cll = 'abcdefgh'
    num = 8
    i = cll.index(cell[0])
    if cll.index(cell[0]) < 1 or cll.index(cell[0]) > 6:
        num //= 2
    elif cll.index(cell[0]) < 2 or cll.index(cell[0]) > 5:
        num -= 2
    if int(cell[1]) < 2 or int(cell[1]) > 7:
        num //= 2
    elif int(cell[1]) < 3 or int(cell[1]) > 6:
        num -= 2
    return num

task = "b1"
print(chessKnight(task))

'''
Given a position of a knight on the standard chessboard,
find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally
and one square vertically, or two squares vertically and one square
horizontally away from it. The complete move therefore looks like the letter L.
Check out the image below to see all valid moves for a knight piece that is placed on
one of the central squares.

Example

    For cell = "a1", the output should be
    chessKnight(cell) = 2.

    For cell = "c2", the output should be
    chessKnight(cell) = 6.

'''