def baseConversion(n, x):
    return hex(int(str(n),x))


n,x = 1302, 5
print(hex(int(str(n),x)))

'''
Now you're bound to win. Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

Example

For n = "1302" and x = 5, the output should be
baseConversion(n, x) = "ca".

Here's why:
13025 = 20210 = ca16.
'''
