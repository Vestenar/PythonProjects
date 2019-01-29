def switchLights(a):
    # if a[0] == a[1] == 1:
    #     a[0] = 0
    # for i in range(1, len(a)):
    #     if a[i - 1] == 1:
    #         if a[i] == 0:
    #             a[i] = 1
    #         else:
    #             a[i] = 0
    for i in range(len(a)):
        if a[i] == 1:
            print(a)
            a[i] = 0
            for j in range(len(a[:i])):
                if a[j] == 1:
                    a[j] = 0
                else:
                    a[j] = 1
    return a


cand = [1, 1, 1, 1, 1]
print(switchLights(cand))