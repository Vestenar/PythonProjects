def arrayMaxConsecutiveSum(inputArray, k):
    s = []
    sm = 0
    for j in range(int(k)):
        sm += inputArray[j]
        ma = sm
    for i in range(1,len(inputArray)-k+1):
        sm -= inputArray[i-1]
        sm += inputArray[i+k-1]
        if ma < sm:
            ma = sm
    return ma

'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

    2 + 3 = 5;
    3 + 5 = 8;
    5 + 1 = 6;
    1 + 6 = 7.
    Thus, the answer is 8.
'''