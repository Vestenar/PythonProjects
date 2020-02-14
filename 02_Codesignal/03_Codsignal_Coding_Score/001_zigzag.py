#определить максимальную длину "зигзага" в массиве
def zigzag(mass):
    le = []
    if len(mass) > 2:
        while len(mass) > 2:
            count = 2
            for i in range(2, int(len(mass))):
                if (mass[i - 2] < mass[i - 1] and mass[i - 1] > mass[i]) or (
                        mass[i - 2] > mass[i - 1] and mass[i - 1] < mass[i]):
                    count += 1
                else:
                    mass = mass[1:]
                    break
            le.append(count)
            mass = mass[1:]
    elif len(mass) == 2:
        if mass[0] == mass[1]:
            le.append(1)
        else:
            le.append(2)
    else:
        le.append(1)
    return max(le)


task = [4, 2, 4, 1, 2, 3, 4, 4, 5, 6]
print(zigzag(task))
