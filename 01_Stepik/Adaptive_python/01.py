str = input("Введи произвольную строку: ")
substr = input("Ведите искомую подстроку: ")

index = str.find(substr)
if index == -1:
    print(index)
else:
    while index!=-1:
        print(index, end = " ")
        index = str.find(substr, (index+1))