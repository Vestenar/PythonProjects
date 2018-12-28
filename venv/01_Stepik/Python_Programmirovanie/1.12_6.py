n = int(input())

if 9 < n < 20 or 9 < n % 10 < 20 or 9 < n % 100 < 20:
    out = "программистов"
elif n % 10 == 1 and n != 11:
    out = "программист"
elif 1 < n % 10 < 5:
    out = "программиста"
else:
    out = "программистов"

print(n, out)