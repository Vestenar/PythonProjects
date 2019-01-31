def reflectString(inputString):
    ans = ""
    for i in inputString:
        ans += (chr(122 + 97 - ord(i)))
    return ans

def reflectString2(inputString):
    return "".join([chr(ord('z') - ord(x) + ord('a')) for x in inputString])

print(reflectString("name"))
print(ord("z"))
print(chr(122))
