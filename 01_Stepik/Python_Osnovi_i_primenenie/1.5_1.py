class MoneyBox:
    def __init__(self, capacity):
        self.value = 0
        self.cap = capacity
    def can_add(self, v):
        return self.value + v <= self.cap
    def add(self, v):
        if self.can_add(v) == True:
            self.value += v


x = MoneyBox(10)
print(x.cap)
x.add(1)
print(x.value)
x.add(11)
print(x.value)
print(x.cap)

'''


Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – 
количеством монет, которые можно положить в копилку. 
Класс должен поддерживать информацию о количестве монет в копилке, 
предоставлять возможность добавлять монеты в копилку и узнавать, 
можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

При создании копилки, число монет в ней равно 0.

Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿.
'''
