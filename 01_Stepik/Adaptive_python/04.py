def split_encode_series(string):
    out = [[string[0], 1]]

    for i in string[1:]:

        if i == out[-1][0]:
            out[-1][1] += 1
        else:
            out.append([i, 1])
    return out


def encode_series(series):
    s = ""
    for [i, n] in series:
        s += (str(n) if n > 1 else "") + i
    return s


def main():
    string = input()
    series = split_encode_series(string)
    print(encode_series(series))


if __name__ == "__main__":
    main()
