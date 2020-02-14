
def convert(num, to_base=10, from_base=10):
    num = int(str(num), base=from_base)
    out = ''
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while num:
        out += alphabet[num % to_base]
        num //= to_base
    return out[::-1]

def check_kaprekar(n):
    n = convert(n)
    if str(n)[1:] and set(str(n)[1:]) == {'0'}:
        return False
    else: return True


def kaprekar(n, base=10):
    if base == 10 and not check_kaprekar(int(n, base=base)): return False
    n = int(n, base=base)
    sq = n** 2
    for base_calc in range(2, 17):
        sq_based = convert(sq, base_calc)
        for i in range(0, len(sq_based) - 1):
            if int(sq_based[i + 1:], base=base_calc) == 0: break
            if int(sq_based[:i + 1], base=base_calc) + int(sq_based[i + 1:], base=base_calc) == n:
                return True
    return False


print(kaprekar('A', 16))
# line = '1, E, 56, 66, EE, 444, 778, EEE, 12XX, 1640, 2046, 2929, 3333, 4973, 5E60, 6060, 7249, 8889, 9293, 9E76, X580, X912, EEEE, 22223, 48730, 72392, 99999, EEEEE, 12E649, 16EX51, 1X1X1X, 222222, 22X54X, 26X952, 35186E, 39X39X, 404040, 4197X2, 450770, 5801E8, 5EE600'
# line16 = '1, 6, 7, A, F, 33, 55, 5B, 78, 88, AB, CD, FE, 15E, 335'     #, 38E, 492, 4ED, 7E0, 820, B13, B6E, C72, CCC, EA1, FA5, FFF, 191A, 2A2B, 3C3C, 4444, 5556, 6667, 7F80, 8080, 9999, AAAA, BBBC, C3C4, D5D5, E6E6, FFFF, 1745E, 20EC2, 2ACAB, 2D02E, 30684, 3831F, 3E0F8, 42108, 47AE1, 55555, 62FCA, 689A3, 7278C, 76417, 7A427, 7FE00, 80200, 85BD9, 89AE5, 89BE9, 8D874, 9765D, 9D036, AAAAB, AF0B0, B851F, BDEF8, C1F08, C7CE1, CF97C, D5355'
# base16 = [i.strip() for i in line16.split(',')]
# for i in base16:
#     print(i, kaprekar(i, 16))
