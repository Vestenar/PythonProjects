a, b = (float(input()) for _ in range(2))
oper = input()

if oper == "+":
    print(a + b)
elif oper == "-":
    print(a - b)
elif oper == "/":
    if b != 0:
        print(a / b)
    else:
        print("Деление на 0!")
elif oper == "*":
    print(a * b)
elif oper == "mod":
    if b !=0:
        print(a % b)
    else:
        print("Деление на 0!")
elif oper == "pow":
    print(a ** b)
elif oper == "div":
    if b !=0:
        print(a // b)
    else:
        print("Деление на 0!")
