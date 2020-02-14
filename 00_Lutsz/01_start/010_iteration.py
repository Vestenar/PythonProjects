listoftuple = [('bob', 35, 'mgr'), ('mel', 40, 'dev')]

s = [age for (name, age, job) in listoftuple]
print(s)
s = list(map((lambda x: x[1]), listoftuple))
print(s)