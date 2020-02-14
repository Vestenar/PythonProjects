def adjacentElementsProduct(inputArray):
    test = inputArray[0]*inputArray[1]
    for i in range((len(inputArray)-2)):
            nmax = inputArray[i+1]*inputArray[i+2]
            if test < nmax:
                test = nmax
    return test


'''
Given an array of integers, find the pair of adjacent 
elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.'''