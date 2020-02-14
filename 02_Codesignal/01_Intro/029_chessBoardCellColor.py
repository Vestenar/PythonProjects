def chessBoardCellColor(cell1, cell2):
    def check(cell):
        a = 0
        if cell[0] in 'ACEG':
            a = 1
        elif cell[0] in 'BDFH':
            a = 0
        if int(cell[1]) <= 8 and int(cell[1]) % 2 == 0:
            a += 1
        return a%2 == 0

    return check(cell1) == check(cell2)

'''
Given two cells on the standard chess board, determine whether they have the same color or not.'''