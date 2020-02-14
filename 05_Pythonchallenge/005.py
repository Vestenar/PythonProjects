import requests
import re

s1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
k = "64196"
# print(16044//2)
while k.isdigit():
    r = requests.get(s1+k).text
    k = re.findall("\d+", r)[0]
# k = re.match("\d+", r)
    print(r)