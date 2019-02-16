import re


def nthNumber(s, n):
    pattern = r"([^1-9]*([0-9]+)){%d}" % n
    return re.match(pattern, s).group(1)


def numRecogniser(num):
    pattern = "([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)"
    return re.findall(pattern, num)


s = "some023020 num ber 033 02103 32 meh peh beh 4328 "
n = 5
print(nthNumber(s, n))

num = "2019e+12-02-15, 0.2, +5.45, -.4, 6e23, -3.17E-14"
print(numRecogniser(num))
'''
You are given a string s of characters that contains at least n numbers 
(here, a number is defined as a consecutive series of digits, where any character 
immediately to the left and right of the series are not digits). 
The numbers may contain leading zeros, but it is guaranteed that each number has 
at least one non-zero digit in it.

Your task is to find the nth number and return it as a string without leading zeros.

Example

For s = "8one 003number 201numbers li-000233le number444" and n = 4,
the output should be
nthNumber(s, n) = "233".
'''
