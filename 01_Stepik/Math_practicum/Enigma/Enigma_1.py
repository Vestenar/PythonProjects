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


for i in 'ABCDUWYGVZS':
    print(rotor(i, 1))