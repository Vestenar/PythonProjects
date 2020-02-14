# Степик. работа с файлами
with open(r'C:\\adb\\dataset_3363_1.txt') as inf:
    s1 = inf.readline()

ans = ''
num = 0
lit = ''
for i in s1:
    if i.isalpha():
        for j in range(int(num)):
            ans += lit
        lit = i
        num = ''
    else:
        num += i
for j in range(int(num)):
    ans += lit
with open(r'C:\\adb\\answer.txt', 'w') as ouf:
    ouf.write(ans)
print(ans)
