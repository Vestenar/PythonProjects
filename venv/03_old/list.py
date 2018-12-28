def arrayMaxConsecutiveSum(inputArray, k):

    sm = 0
    for j in range(int(k)):
        sm += inputArray[j]
    ma = sm
    for i in range(len(inputArray)-k):
        sm -= inputArray[i]
        sm += inputArray[i+k]
        if ma < sm:
            ma = sm
    return ma


test = [2, 3, 5, 1, 6]
ke = 2
print(arrayMaxConsecutiveSum(test, ke))
