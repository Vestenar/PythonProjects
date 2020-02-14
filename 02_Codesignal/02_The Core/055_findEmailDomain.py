import re
def findEmailDomain(address):

    return re.findall(r'@([a-zA-Z]+.\w+)',address)[0]


addr = "<>[]:,;@\"!#$%&*+-/=?^_{}| ~.a\"@example.org"
print(findEmailDomain(addr))