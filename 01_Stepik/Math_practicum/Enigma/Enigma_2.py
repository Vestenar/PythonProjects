def reflector(symbol, n):
    if n == 0: return symbol

    reflectors = {1: [i[1:-1] for i in '(AY) (BR) (CU) (DH) (EQ) (FS) (GL) (IP) (JX) (KN) (MO) (TZ) (VW)'.split()], # B-type
                  2: [i[1:-1] for i in '(AF) (BV) (CP) (DJ) (EI) (GO) (HY) (KR) (LZ) (MX) (NW) (TQ) (SU)'.split()], # C-type
                  }
    for cycle in reflectors[n]:
        if symbol in cycle:
            return cycle[(cycle.index(symbol) + 1) % len(cycle)]




