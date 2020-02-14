def twoTeams(students):
    return sum(students[::2]) - sum(students[1::2])



students = [1, 11, 13, 6, 14]
print(twoTeams(students))

students = [3]
print(twoTeams(students))

students = [16, 14, 79, 8, 71, 72, 71, 10, 80, 76, 83, 70, 57, 29, 31]
print(twoTeams(students))


