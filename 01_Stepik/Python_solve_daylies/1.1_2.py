from urllib.request import urlopen
import re

urlfile = urlopen(r'https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')
sfile = str(urlfile)
pattern = r'(?<=<code>).*?(?=<\/code>)'
s = re.findall(pattern, sfile)
# print(sorted(s))
printed = {}
max_cnt = 0
for item in s:
    if item not in printed:
        cnt = s.count(item)
        printed[item] = cnt
        if cnt > max_cnt: max_cnt = cnt

for elem, cnt in printed.items():
    if cnt == max_cnt:
        print(elem, end=' ')