class MyList(list):
    def __init__(self, lst):
        self.wrapped = []
        for i in lst:
            self.wrapped.append(i)

    def __add__(self, other):
        # self.wrapped += other
        return MyList(self.wrapped + other)

    def __radd__(self, other):
        self.wrapped += other
        return self.wrapped

    def __mul__(self, mul):
        return self.wrapped * mul

    def __getitem__(self, index):
        return self.wrapped[index]

    def __setitem__(self, key, value):
        self.wrapped[key] = value

    def __len__(self):
        l = len(self.wrapped)
        print('Length of list is %d' % l)
        return l

    def __repr__(self):
        return repr(self.wrapped)



if __name__ == '__main':

    mlst = MyList([1, 2, 3, 4])
    print(mlst)
    print(mlst + [4, 3, 2, 1])
    print(mlst[2])
    mlst[1] = '00'
    print(mlst)
    print(mlst[1:3])
    print(mlst*3)
    print(mlst)
    print([0,0,1,0] + mlst)
    print(len(mlst))
