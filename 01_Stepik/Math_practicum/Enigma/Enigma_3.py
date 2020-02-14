def enigma(text, ref, rot1, rot2, rot3):
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
                return cycle[(cycle.index(symbol) + 1 - 2 * reverse) % len(cycle)]

    def reflector(symbol, n):
        if n == 0: return symbol

        reflectors = {
            1: [i[1:-1] for i in '(AY) (BR) (CU) (DH) (EQ) (FS) (GL) (IP) (JX) (KN) (MO) (TZ) (VW)'.split()],
            2: [i[1:-1] for i in '(AF) (BV) (CP) (DJ) (EI) (GO) (HY) (KR) (LZ) (MX) (NW) (TQ) (SU)'.split()],
            }
        for cycle in reflectors[n]:
            if symbol in cycle:
                return cycle[(cycle.index(symbol) + 1) % len(cycle)]

    line = [rot3, rot2, rot1]
    cypher = ''
    text = text.replace(' ', '').upper()

    for i in range(3):
        for char in text:
            cypher += rotor(char, line[i])
        text, cypher = cypher, ''

    for char in text:
        cypher += reflector(char, ref)
    text, cypher = cypher, ''

    for j in range(3):
        for char in text:
            cypher += rotor(char, line[2-j], True)
        text, cypher = cypher, ''
    return text


print(
      enigma('A', 1, 1, 0, 0),
      enigma('A', 1, 1, 2, 3),
      enigma('U', 1, 1, 2, 3),
      enigma('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1, 1, 2, 3),
      enigma('Some encripted text', 1, 1, 2, 3),
      enigma('LDRBBKJMWGFBOFBYF', 1, 1, 2, 3),
      sep='\n'+'-'*80+'\n')
