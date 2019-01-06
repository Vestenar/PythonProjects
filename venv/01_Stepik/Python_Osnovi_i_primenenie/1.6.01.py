class MyList(list):
    def even_lenght(self):
        return len(self)%2==0


x = MyList()
print(x)
x.extend([1,2,3,4,5])
print(x)
print(x.even_lenght())
x.append(6)
print(x)
print(x.even_lenght())