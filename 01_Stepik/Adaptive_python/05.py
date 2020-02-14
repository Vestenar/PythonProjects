def cipher(s, n):
    alph = ' abcdefghijklmnopqrstuvwxyz'

    out = ""
    for i in s:
        out += alph[(alph.index(i) + n) % 27]

    print('Result: "{}"'.format(out))


def main():
    shift = int(input())
    s = input().strip()
    cipher(s, shift)


if __name__ == "__main__":
    main()
