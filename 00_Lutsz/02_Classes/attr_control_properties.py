class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value
    name = property(getName, setName)

    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise TypeError('wrong age')
        else:
            self.__age = value
    age = property(getAge, setAge)

    def getAcc(self):
        return self.__acct[:3] + '***'

    def setAcc(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:                  # from self
            raise TypeError('wrong account number')
        else:
            self.__acct = value
    acct = property(getAcc, setAcc)

    def remainGet(self):
        return self.retireage - self.age
    remain = property(remainGet)


bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
bob.name = 'Bob Q. Smith'
bob.age = 50
bob.acct = '23-45-67-89'
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
print(sue.acct, sue.name, sue.age, sue.remain, sue.addr, sep=' / ')
try:
    sue.age = 200
except:
    print('Bad age for Sue')
try:
    sue.remain = 5
except:
    print("Can't set sue.remain")
try:
    sue.acct = '1234567'
except:
    print('Bad acct for Sue')
