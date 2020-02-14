# -*- coding: IBM866 -*-

import sys

OZ = 'NO'


class InfoFromAY:
    def __init__(self, data):
        self.words = {x: data[x] for x in range(len(data))}
        self.GN = angle(data[0])
        self.VN = angle(data[1])
        self.RRR = 'ON' if int(data[2], 16) & int('1000', 16) else 'OFF'
        self.DU = 'ON' if int(data[2], 16) & int('0800', 16) else 'OFF'
        self.GOT = 'ON' if int(data[2], 16) & int('0400', 16) else 'OFF'
        self.SOST_PRIV = bin(int(data[2], 16))[-10:-8] # & int('0300', 16)
        self.ZTN = 'YES' if int(data[2], 16) & int('0080', 16) else 'NO'
        self.ZTV = 'YES' if int(data[2], 16) & int('0040', 16) else 'NO'
        self.ZTL = 'YES' if int(data[2], 16) & int('0008', 16) else 'NO'
        self.ZTP = 'YES' if int(data[2], 16) & int('0004', 16) else 'NO'
        self.PVN = 'Pohod VN' if int(data[2], 16) & int('0020', 16) else 'NO'
        self.PGN = 'Pohod GN' if int(data[2], 16) & int('0002', 16) else 'NO'
        self.RAS = 'Rassoglas' if int(data[2], 16) & int('0001', 16) else 'OK'
        self.OTKAZ = int(data[3], 16) & int('01FF', 16)
        self.POZ = 'OPAS ZONA!' if int(data[4], 16) & int('0400', 16) else 'OK'
        self.STOPOR = 'ON' if int(data[4], 16) & int('0020', 16) else 'OFF'
        self.OHL = 'ON' if int(data[4], 16) & int('0010', 16) else 'OFF'
        self.CS2 = 'ON' if int(data[4], 16) & int('0008', 16) else 'OFF'
        self.CS1 = 'ON' if int(data[4], 16) & int('0004', 16) else 'OFF'
        self.PRIV_VKL = 'ON' if int(data[4], 16) & int('0001', 16) else 'OFF'
        self.RAB = 'ON' if int(data[3], 16) & int('8000', 16) else 'OFF'  # ???? OO ???
        global OZ
        if self.POZ != 'OK':
            OZ = 'Priznak poluchen'

    def print(self):
        # print(self.words)
        print('Rabota:', self.RAB, '  CS:', self.CS1, self.CS2, ' OHL:', self.OHL, '  Privod, DU:', self.PRIV_VKL, self.DU, '  RRR:', self.RRR, end='  ')
        print('OZ:', self.POZ, ' Otkaz:', self.OTKAZ, ' Gotovnost:', self.GOT, ' Sost. Privod:', self.SOST_PRIV, ' Rassoglas:', self.RAS, self.PVN, self.PGN)
        print(('{:.1f} mil ... {:.1f} mil').format(self.GN, self.VN))
        pass


class InfoToAY:
    def __init__(self, data):
        self.words = {x: data[x] for x in range(len(data))}
        self.GN = angle(data[0])
        self.VN = angle(data[1])
        self.RKCm = int(data[2], 16) & int('4000', 16)  # результат самоконтроля
        self.PDU = int(data[4], 16) & int('0400', 16)  # передача управления
        self.RAB = 'ON' if int(data[4], 16) & int('0080', 16) else 'OFF'
        self.OHL = 'ON' if int(data[4], 16) & int('0020', 16) else 'OFF'
        self.CS1 = 'ON' if int(data[4], 16) & int('0010', 16) else 'OFF'
        self.CS2 = 'ON' if int(data[4], 16) & int('0008', 16) else 'OFF'
        self.PRIV = 'ON' if int(data[4], 16) & int('0004', 16) else 'OFF'
        self.DU = 'ON' if int(data[4], 16) & int('0002', 16) else 'OFF'
        self.RRR = 'ON' if int(data[4], 16) & int('0001', 16) else 'OFF'

    def print(self):
        # print(self.words)
        # print(self.RKCm), print(self.PDU)
        # print(bin(int(self.words[4], base=16)))
        # print(self.words[4])
        print('Rabota:', self.RAB, '  CS:', self.CS1, self.CS2, ' OHL:', self.OHL, '  Privod, DU:', self.PRIV, self.DU, '  RRR:', self.RRR)
        print(('{:.1f} mil ... {:.1f} mil').format(self.GN, self.VN))
        pass


def angle(angle_str):
    lim = 0x7FFF
    angle = int(angle_str, 16)
    sign = angle & int('8000', 16)

    return angle  * 1500 / 16384 if not sign else (angle - 0xFFFF) * 1500 / 16384


def parser(line):
    if line.startswith('      ИС:'):
        data = line.split(':')[1].strip().split()
        if len(data) == 10:
            print('Из АУ: ', end='')
            InfoFromAY(data).print()
        elif len(data) == 8:
            print('В АУ:  ', end='')
            InfoToAY(data).print()
    elif line.startswith(' 0:'):
        n = int(line.split(':')[1])
        if n % 2 == 0: print('_____Seans obmena: %d_______'% n)


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input('Введите имя файла для разбора: >> ')
    if not filename:
        filename = '630_1.txt'

# count = 50000
with open(filename, 'r', encoding='cp866') as file:
    for line in file:
        parser(line)
        # count -= 1
        # if not count: break
print('\n', 'opaznaya zona: ', OZ)
exit()
