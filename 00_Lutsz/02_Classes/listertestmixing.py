from lister import *


class Super():
    def __init__(self):
        self.data1 = 'one'

    def ham(self):
        pass


class Sub(Super, ListInstance):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'two'
        self.data3 = 'three'

    def spam(self):
        pass


class Sub2(Super, ListInherited):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'two'
        self.data3 = 'three'

    def spam(self):
        pass


class Sub3(Super, ListTree):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'two'
        self.data3 = 'three'

    def spam(self):
        pass


x = Sub()
print(x)
print('_' * 50, '\n\n')

y = Sub2()
print(y)
print('_' * 50, '\n\n')

z = Sub3()
print(z)
