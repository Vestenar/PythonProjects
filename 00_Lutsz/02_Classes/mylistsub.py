from mylist import MyList


class MyListSub(MyList):
    calls = 0

    def __init__(self, lst):
        self.adds = 0
        MyList.__init__(self, lst)

    def __add__(self, other):
        print('adding')
        self.adds += 1
        MyListSub.calls += 1
        return MyList.__add__(self, other)

    def __len__(self):
        print('getting len')
        return MyList.__len__(self)

    def stats(self):
        return self.calls, self.adds


# x = MyListSub([1,2,3,4])
# print(type(x))
# print(x[2])
# print(x[:2])
# y = MyListSub(list('spam'))
# print(y)
# print(type(y))
# len(x)
# print(x + [5,6,7])
# print(x + [1])
# print(type(x))
#
# print(x.stats())
x = MyListSub('spam')
y = MyListSub('foo')
print(x[2])
print(x[1:])
print(x + ['eggs'])
print(x + ['toast'])
print(y + ['bar'])
print(x.stats())
