
m, n = map(int, input().split())

if n + m > 4 and (n + m) % 2 == 1:
    print('Замостить можно')
else:
    print('Замостить нельзя')