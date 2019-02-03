def arrayConversion(inputArray):
    sum = True
    while len(inputArray) > 1:
        if sum:
            temp = [inputArray[i] + inputArray[i+1] for i in range(0, len(inputArray), 2)]
        else:
            temp = [inputArray[i] * inputArray[i+1] for i in range(0, len(inputArray), 2)]
        inputArray = temp[:]
        sum = not sum
    return inputArray[0]


ia = [1, 2, 3, 4, 5, 6, 7, 8]
print(arrayConversion(ia))
ia = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(arrayConversion(ia))
ia = [3, 3, 5, 5]
print(arrayConversion(ia))
'''
Given an array of 2k integers (for some integer k), perform the following operations until
the array contains only one element:

    On the 1st, 3rd, 5th, etc. iterations (1-based) replace each pair of consecutive elements with their sum;
    On the 2nd, 4th, 6th, etc. iterations replace each pair of consecutive elements with their product.

After the algorithm has finished, there will be a single element left in the array. Return that element.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8], the output should be
arrayConversion(inputArray) = 186.

We have [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186], so the answer is 186.
'''
