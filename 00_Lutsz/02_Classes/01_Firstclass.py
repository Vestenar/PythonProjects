#!/usr/local/bin/python
class FirstClass:
    def setdata(self, value):
        self.data = value
    def showdata(self):
        print(self.data)

class SecondClass(FirstClass):
    def showdata(self):
        print('Current value = "%s"' % self.data)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[Third Class: %s]' % self.data



x = FirstClass()
y = FirstClass()

x.setdata(1234)
y.setdata("DATA FOR Y")

x.showdata()
y.showdata()

x.setdata("string")
x.showdata()

x.another = "345"
print(x.another)

z = SecondClass()
z.setdata(42)
z.showdata()
#print(dir(x))

a = ThirdClass("abc")
a.showdata()
print(a)

b = a + 'zxq'
b.showdata()
print(b)