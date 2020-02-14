def decipher(s):
    n = 1
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i-1].isdigit():
                n = 10 * n + int(s[i])
            else:
                n = int(s[i])
        else:
            out = n * s[i]
            n = 1
            yield out



def main():
    s = input().strip()
    for i in decipher(s):
        print(i, end="")


if __name__ == "__main__":
    main()
