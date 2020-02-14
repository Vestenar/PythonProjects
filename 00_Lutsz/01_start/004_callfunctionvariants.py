def echo(msg):
    print(msg)


echo("Direct")

x = echo
x("Indirect")


# функции легко можно передавать другим
# функциям в виде аргументов
def indirect(func, arg):
    func(arg)


indirect(echo, "Argument call")

schedule = [(echo, "One"), (echo, "Two")]
# наполнять структуры данных функциями, как
# если бы они были простыми числами или строками
for func, arg in schedule:
    func(arg)


# функции могут также создаваться и возвращаться другими функциями
def make(label):
    def echo2(msg):
        print(label + ":" + msg)
    return echo2


F = make("super")
F("sudo")
D = make("puper")
D("admin")

print(dir(make))
print((F.__name__))