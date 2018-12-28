
def isIPv4Address(inputString):
    ip4 = [i for i in inputString.split(sep='.')]
    if len(ip4) != 4:
        return False
    for i in range(4):
        if ip4[i].isnumeric() == False:
            return False
        else:
            ip4[i] = int(ip4[i])

    return len(ip4) == 4 and (0 <= ip4[0] < 256) and (0 <= ip4[1] < 256) and (0 <= ip4[2] < 256) and (0 <= ip4[3] < 256)

'''
IPv4 addresses are represented in dot-decimal notation, 
which consists of four decimal numbers, each ranging from 0 to 255 inclusive, 
separated by dots, e.g., 172.16.254.1.

Given a string, find out if it satisfies the IPv4 address naming rules.'''