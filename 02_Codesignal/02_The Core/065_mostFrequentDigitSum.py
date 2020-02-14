def mostFrequentDigitSum(n):
    sums = {}
    while n > 0:
        s = sum(map(int, str(n)))
        n -= s
        if s in sums:
            sums[s] += 1
        else: sums[s] = 1
    a = max(sums.values())
    inv_sums = {val: key for key, val in sums.items()} # инверсия словаря
    return inv_sums[a]

print(mostFrequentDigitSum(999999))

'''
A step(x) operation works like this: 
it changes a number x into x - s(x), where s(x) is the sum of x's digits. 

You like applying functions to numbers, so given the number n, 
you decide to build a decreasing sequence of numbers: 
n, step(n), step(step(n)), etc., with 0 as the last element.

Building a single sequence isn't enough for you, so you replace 
all elements of the sequence with the sums of their digits (s(x)). 
Now you're curious as to which number appears in the new sequence most often. 
If there are several answers, return the maximal one.

Example

    For n = 88, the output should be
    mostFrequentDigitSum(n) = 9.
        Here is the first sequence you built: 88, 72, 63, 54, 45, 36, 27, 18, 9, 0;
        And here is s(x) for each of its elements: 16, 9, 9, 9, 9, 9, 9, 9, 9, 0.

    As you can see, the most frequent number in the second sequence is 9.

    For n = 8, the output should be
    mostFrequentDigitSum(n) = 8.
        At first you built the following sequence: 8, 0
        s(x) for each of its elements is: 8, 0

    As you can see, the answer is 8 (it appears as often as 0, but is greater than it).

'''
