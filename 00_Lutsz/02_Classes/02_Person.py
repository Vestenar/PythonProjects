#!/usr/local/bin/python
class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def info(self):
        return (self.name, self.job)

man1 = Person("John", "QA")
man2 = Person("Mel", "Dev")

print(man1.job)
print(man2.info())
