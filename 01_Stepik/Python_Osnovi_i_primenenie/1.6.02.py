# наследование классов

class EvenLenghtMixing:
    def even_lenght(self):
        return len(self) % 2 ==0


class MyList(list, EvenLenghtMixing):
    def pop(self):
        x = super(MyList, self).pop()  # определить метод так, будто он не определен в родительском классе
        print("Last value is:", x)
        return x

print(MyList.mro())  # method resolution order - порядок разрешения методов

x = MyList([1,2,3,4,5])
print(x)
print(x.even_lenght())
x.append(6)
print(x)
print(x.even_lenght())

ml = MyList([1,2,3,17])
z = ml.pop()
print(z)
print(ml)