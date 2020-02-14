import requests
import re

# url1, url2, a = (input() for i in range(3))
# res1 = requests.get(url1).text
# res2 = url2
# print(res2)
# pattern = r'http.*?html'
# lst = re.findall(pattern, res1)
# lst2 = []
# for i in range(len(lst)):
#     res = requests.get(lst[i]).text
#     lst2+=(re.findall(pattern, res))
# # print(lst2)
# print(re.findall(pattern, res2))
# if re.findall(pattern, res2)[0] in lst2:
#     print("Yes")
# else:
#     print("No")

# решение с другой регуляркой
start_url = input()
end_url = input()

found = False

link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
resp = requests.get(start_url).text

for url in link_pattern.findall(resp):
    cur_resp = requests.get(url).text
    if end_url in link_pattern.findall(cur_resp):
        found = True
        break

print("Yes" if found else "No")