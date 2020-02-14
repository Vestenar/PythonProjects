a, b, c = (int(input()) for _ in range(3))
max_ = c
min_ = c

if a >= b and a >= c:
    max_ = a
elif b > c:
    max_ = b

if a <= b and a <= c:
    min_ = a
elif b < c:
    min_ = b

print(max_, '\n', min_, '\n', a + b + c - min_ - max_)