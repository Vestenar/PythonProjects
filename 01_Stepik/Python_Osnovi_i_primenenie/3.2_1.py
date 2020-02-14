# s = "abab"
# a = "ab"
# b = "ba"
s,a,b = (input() for i in range(3))
count = 0

while a in s:
    count += 1
    s = s.replace(a,b)
    if count == 1000:
        count = "Impossible"
        break
print(count)



