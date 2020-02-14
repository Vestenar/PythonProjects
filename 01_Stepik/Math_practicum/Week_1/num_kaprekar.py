def kaprekar(n):
    sq = str(n**2)
    print(sq)
    for i in range(0, len(sq) - 1):
        print(sq[:i + 1], '____', sq[i + 1:])
        if int(sq[i + 1:]) == 0: break
        if int(sq[:i + 1]) + int(sq[i + 1:]) == n:
            return True
    return False

print(kaprekar(10000))