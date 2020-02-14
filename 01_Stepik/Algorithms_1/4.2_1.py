coder = {}

def code(s):
    freq = []
    global coder
    for l in list(set(s)):
        freq.append((l, s.count(l)))

    while len(freq) > 1:
        freq.sort(key=lambda x: x[1])
        a = freq.pop(0)
        b = freq.pop(0)
        freq.append([[a[0], b[0]], a[1] + b[1]])
    freq = freq[0][0]
    if len(freq) > 1:
        recur(freq, "")
    else:
        coder[freq] = "0"
    ans = "".join(coder[i] for i in s)
    print(len(set(s)), len(ans))
    for key in coder:
        print(key +": " + coder[key])
    print(ans)
    return


def recur(lst, st):
    global coder
    lstl, lstr = lst[0], lst[1]
    sl, sr = st + "0", st + "1"
    if type(lstl) == str:
        coder[lstl] = sl
    else: recur(lstl, sl)
    if type(lstr) == str:
        coder[lstr] = sr
    else: recur(lstr, sr)

def main():
    s = input()
    code(s)


if __name__ == "__main__":
    main()
