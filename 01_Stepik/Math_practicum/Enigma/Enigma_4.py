def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    def rotor(symbol, n, reverse=False):
        rotors = {1: [i[1:-1] for i in '(AELTPHQXRU) (BKNW) (CMOY) (DFG) (IV) (JZ) (S)'.split()],
                  2: [i[1:-1] for i in '(FIXVYOMW) (CDKLHUP) (ESZ) (BJ) (GR) (NT) (A) (Q)'.split()],
                  3: [i[1:-1] for i in '(ABDHPEJT) (CFLVMZOYQIRWUKXSG) (N)'.split()],
                  4: [i[1:-1] for i in '(AEPLIYWCOXMRFZBSTGJQNH) (DV) (KU)'.split()],
                  5: [i[1:-1] for i in '(AVOLDRWFIUQ)(BZKSMNHYC) (EGTJPX)'.split()],
                  6: [i[1:-1] for i in '(AJQDVLEOZWIYTS) (CGMNHFUX) (BPRK)'.split()],
                  7: [i[1:-1] for i in '(ANOUPFRIMBZTLWKSVEGCJYDHXQ)'.split()],
                  8: [i[1:-1] for i in '(AFLSETWUNDHOZVICQ) (BKJ) (GXY) (MPR)'.split()],
                  'beta': [i[1:-1] for i in '(ALBEVFCYODJWUGNMQTZSKPR) (HIX)'.split()],
                  'gamma': [i[1:-1] for i in '(AFNIRLBSQWVXGUZDKMTPCOYJHE)'.split()],
                  }
        if n == 0: return symbol

        for cycle in rotors[n]:
            if symbol in cycle:
                return cycle[(cycle.index(symbol) + 1 * (-1)**reverse) % len(cycle)]

    def reflector(symbol, n):
        if n == 0: return symbol

        reflectors = {
            1: [i[1:-1] for i in '(AY) (BR) (CU) (DH) (EQ) (FS) (GL) (IP) (JX) (KN) (MO) (TZ) (VW)'.split()],
            2: [i[1:-1] for i in '(AF) (BV) (CP) (DJ) (EI) (GO) (HY) (KR) (LZ) (MX) (NW) (TQ) (SU)'.split()],
            }
        for cycle in reflectors[n]:
            if symbol in cycle:
                return cycle[(cycle.index(symbol) + 1) % len(cycle)]

    def caesar(txt, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        alphabet_dict = dict(enumerate(alphabet))

        txt = ''.join(i.upper() for i in txt if i.isalnum())
        crypted = ''.join([alphabet_dict[(alphabet.index(i) + key) % len(alphabet)] for i in txt])
        return crypted

    line = [rot3, rot2, rot1]
    shift = [shift3, shift2, shift1]
    cypher = ''

    for char in text.upper():
        if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            continue
        for i in range(3):
            char = caesar(rotor(caesar(char, shift[i]), line[i]), -shift[i])

        char = reflector(char, ref)

        for j in range(3):
            char = caesar(rotor(caesar(char, shift[2-j]), line[2-j], True), -shift[2-j])
        cypher += char

    return cypher


print(
    enigma('A', 1, 0, 0, 0, 0, 3, 2),
    enigma('B', 1, 1, 0, 2, 0, 3, 2),
    enigma('A', 1, 1, 0, 2, 1, 3, 1),
    enigma('A', 1, 1, 1, 2, 2, 3, 1),
    enigma('Some encripted text', 1, 1, 1, 2, 2, 3, 1),
    enigma('Some encripted text', 1, 1, -1, 2, 2, 3, -1),
    enigma('AYIQQLXZMFHQUHQCH', 1, 1, -1, 2, 2, 3, -1),

    sep='\n'+'-'*80+'\n')
