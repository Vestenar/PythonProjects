class Adder:
    def __init__(self, initial=[]):
        self.initial = initial

    def add(self, x, y):
        return x + y

    def __add__(self, other):
        # self.out = self.initial + other
        return self.add(self.initial, other)


class ListAdder(Adder):
    def add(self, y):
        return self.initial + y


class DictAdder(Adder):
    def add(self, x, y):
        x.update(y)
        return x


a1 = Adder([1,2])
print(a1.add(2, 3))
print(a1 + [2,3])


a2 = ListAdder([1, 2, 3, 4])
print(a2.add(['a', 'b']))


a3 = DictAdder()
print(a3.add({1: '1', 2: '2'}, {3: '3'}))
print('reloaded')
