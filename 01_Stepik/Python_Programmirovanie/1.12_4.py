exec('''
strType = input()
if strType == "треугольник":
    a, b, c = (int(input()) for _ in range(3))
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif strType == "прямоугольник":
    a, b = (int(input()) for _ in range(2))
    print(a * b)
elif strType == "круг":
    a = int(input())
    print(3.14 * a ** 2)
''')