n = int(input())
a = int(n // 1e5)
b = int((n % 1e5) // 1e4)
c = int((n % 1e4) // 1e3)
d = (n % 1000) // 100
e = (n % 100) // 10
f = n % 10

if a + b + c == d + e + f:
    out = "Счастливый"
else:
    out = "Обычный"

print(out)