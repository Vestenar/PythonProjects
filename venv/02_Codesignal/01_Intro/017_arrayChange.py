def arrayChange(inputArray):
    n = 0
    for i in range(1, len(inputArray)):
        while inputArray[i] <= inputArray[i-1]:
            n += inputArray[i - 1] - inputArray[i] + 1
            inputArray[i] += inputArray[i-1] - inputArray[i] +1
    return n


'''
You are given an array of integers. On each move you are allowed to increase 
exactly one of its element by one. Find the minimal number of moves required 
to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.'''