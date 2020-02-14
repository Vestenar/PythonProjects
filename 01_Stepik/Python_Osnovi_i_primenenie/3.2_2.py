# s = "abababa"
# t = "aba"

s, t = (input() for i in range(2))
count = 0

while t in s:
    count += 1
    s = s[s.index(t)+1:]
print(count)