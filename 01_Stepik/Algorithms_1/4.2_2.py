def decode(k):
    decoder = {}
    ans = ""
    for i in range(k):
        key, val = input().split(":")
        decoder[val.strip()] = key
    code = input()
    i = 1
    while code:
        if code[:i] in decoder:
            ans += decoder[code[:i]]
            code = code[i:]
            i = 1
        else:
            i+=1
    print(ans)
    return

def main():
    k, l = map(int, input().split())
    decode(k)

if __name__ == "__main__":
    main()