def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
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

    reflectors = {
            1: [i[1:-1] for i in '(AY) (BR) (CU) (DH) (EQ) (FS) (GL) (IP) (JX) (KN) (MO) (TZ) (VW)'.split()],
            2: [i[1:-1] for i in '(AF) (BV) (CP) (DJ) (EI) (GO) (HY) (KR) (LZ) (MX) (NW) (TQ) (SU)'.split()],
            }

    shift_cond = {1: [17], 2: [5], 3: [22], 4: [10], 5: [0], 6: [0, 13], 7: [0, 13], 8: [0, 13]}

    def rotor(symbol, n, reverse=False):
        if n == 0: return symbol

        for cycle in rotors[n]:
            if symbol in cycle:
                return cycle[(cycle.index(symbol) + 1 * (-1)**reverse) % len(cycle)]

    def reflector(symbol, n):
        if n == 0: return symbol

        for cycle in reflectors[n]:
            if symbol in cycle:
                return cycle[(cycle.index(symbol) + 1) % len(cycle)]

    def caesar(txt, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        alphabet_dict = dict(enumerate(alphabet))

        txt = ''.join(i.upper() for i in txt if i.isalnum())
        crypted = ''.join([alphabet_dict[(alphabet.index(i) + key) % len(alphabet)] for i in txt])
        return crypted

    def rotate(shift_in, line_in):

        next_rot[0] = 1
        for k in range(n_rot):
            shift_in[k] = (shift_in[k] + next_rot[k]) % 26
        next_rot[1:] = [0, 0]

        for n in range(n_rot - 1):
            if shift_in[n] + 1 in shift_cond[line_in[n]]:
                next_rot[n] = 1
                next_rot[n + 1] = 1
                break
        return shift_in

    def check_pairs(comm_pairs):
        comm_pairs = comm_pairs.replace(' ', '').upper()
        for ch in comm_pairs:
            if comm_pairs.count(ch) > 1:
                return False
        return True

    def commute(char_c):
        for pair in pairs:
            if char_c in pair:
                char_c = pair[(pair.index(char) + 1) % 2]
        return char_c

    if not check_pairs(pairs):
        return 'Извините, невозможно произвести коммутацию'

    pairs = [i.upper() for i in pairs.split()]
    n_rot = 3
    line = [rot3, rot2, rot1]
    shift = [shift3, shift2, shift1]
    cypher = ''
    next_rot = [1, 0, 0]

    for char in text.upper():

        if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            continue

        char = commute(char)
        shift = rotate(shift, line)

        for i in range(n_rot):
            char = caesar(rotor(caesar(char, shift[i]), line[i]), -shift[i])

        char = reflector(char, ref)

        for j in range(n_rot):
            char = caesar(rotor(caesar(char, shift[2-j]), line[2-j], True), -shift[2-j])
        char = commute(char)
        cypher += char

    return cypher


print(
    enigma('A', 1, 1, 0, 2, 0, 3, 0, ''),
    enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC'),
    enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd'),
    enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd az'),
    enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd za'),
    enigma('AAAAAAA', 1, 1, 0, 2, 0, 3, 0),
    enigma('AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA', 1, 2, 3, 2, 3, 2, 3, 'AC qd zv'),

    sep='\n'+'-'*80+'\n')
