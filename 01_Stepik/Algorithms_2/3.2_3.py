def get_hash(string):
    hash = 0
    ind = 0
    xe = xs.copy()
    for ch in string:
        hash += (ord(ch) * xe[ind]) % p
        ind += 1
    return hash % p


p = 1000000007
x = 263
xs = []         # powers of x[i]

# pattern = input().strip()
# text = input().strip()
pattern = 'a' * 40000
text = 'a' * 80000

lp = len(pattern)
for i in range(lp):
    xs.append(pow(x, i, p))

pattern_hash = get_hash(pattern)
text_hash = get_hash(text[-lp:])
positions = []
lt = len(text)
# for i in range(lt - lp):
#     if text_hash == pattern_hash:
#         positions.append(lt - lp)
#     text_hash = (((text_hash - xs[-1] * ord(text[-1])) * x) % p + ord(text[-(lp + 1)])) % p
#     text = text[:-1]
#     lt -= 1

for i in range(lt-lp, -1, -1):
    if text_hash == pattern_hash:
        positions.append(i)
    text_hash = (text_hash - ord(text[i + lp - 1]) * xs[lp - 1]) % p
    text_hash = (text_hash + p) % p
    text_hash = (text_hash * x) % p
    text_hash = (text_hash + ord(text[i - 1])) % p

if text_hash == pattern_hash:
    positions.append(0)
print(*positions[::-1])
