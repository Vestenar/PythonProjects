def chessKnightMoves(cell):
    cll = 'abcdefgh'
    count=0
    for turn in [[i,j] for i in [-2,-1,1,2] for j in [-2,-1,1,2] if abs(i) !=abs(j)]:
        print(turn)
        x=cll.index(cell[0])+turn[0]
        y=int(cell[1])+turn[1]
        if x >= 0 and x <= 7 and y >= 1 and y <= 8:
            count+=1
    return count

print(chessKnightMoves("a4"))