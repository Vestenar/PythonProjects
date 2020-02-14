a, b = int(input()), int(input())
pie = 1
while pie % a > 0 or pie % b > 0:
    pie += 1
print(pie)