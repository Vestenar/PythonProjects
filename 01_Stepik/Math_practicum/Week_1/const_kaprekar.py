def numerics(n):
    return [int(i) for i in str(n)]

def kaprekar_step(L):
    a = int("".join(map(str, sorted(L))))
    b = int("".join(map(str, sorted(L)[::-1])))
    return abs(a - b)

def kaprekar_loop(n):
    n_prev = 1
    used = []
    if not kaprekar_check(n):
        print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')
        return
    else:
        while n != n_prev:
            used.append(n)
            print(n)
            n_prev = n
            n = kaprekar_step(numerics(n))
            if n in used[:-1]:
                print(f'Следующее число - n, кажется процесс зациклился...')
                return

def kaprekar_check(n):
    n = str(n)
    if len(n) in [3, 4, 6] and len(set(n)) != 1 and n not in ['100', '1000', '100000']:
        return True
    else:
        return False

kaprekar_loop(103303)