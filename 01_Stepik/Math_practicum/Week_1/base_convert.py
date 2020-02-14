def convert(num, to_base=10, from_base=10):
    num = int(str(num), base=from_base)
    out = ''
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while num:
        out += alphabet[num % to_base]
        num //= to_base
    return out[::-1]

print(convert(42, 35))

