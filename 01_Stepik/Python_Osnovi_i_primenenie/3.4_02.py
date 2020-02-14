import re, requests
import pprint

document = requests.get('http://pastebin.com/raw/hfMThaGb').text

addr_list = []
pattern = r"<a.*?href=['\"]?(https?://|ftp://)?(?:(\w[-_.\da-z]*))"
for text in re.findall(pattern, document):
    if text[1] not in addr_list:
        addr_list.append(text[1])
addr_list.sort()
pprint.pprint(addr_list)
