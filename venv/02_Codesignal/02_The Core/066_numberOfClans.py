def numberOfClans(divisors, k):
    divisors = list(set(divisors))
    clans = {k: [] for k in range(1, k + 1)}
    ans = []
    for i in range(1, k+1):
        for div in divisors:
            if i % div == 0:
                a = clans[i]
                a.append(div)
                clans[i] = a
    for key, val in clans.items():
        if val not in ans:
            ans.append(val)
    return len(ans)


divisor = [6, 2, 2, 8, 9, 2, 2, 2, 2]
kk = 10
print(numberOfClans(divisor, kk))

# divisors = [2, 6, 8, 9] (duplicates don't matter in divisors).
#
# 1,3,5,7 are divisible by none of those, 1 clan
# 2,4,10 are divisible by only 2 among these, 1 clan
# 6 is divisible by 2,6 among these, 1 clan.
# 8 is divisible by 2,8 among these, 1 clan.
# 9 is divisible by only 9 among these, 1 clan.
#
# Total is 5 clans.

'''
Let's call two integers A and B friends 
if each integer from the array divisors is either a divisor of both A and B or neither A nor B. 
If two integers are friends, they are said to be in the same clan. 
How many clans are the integers from 1 to k, inclusive, broken into?

Example

For divisors = [2, 3] and k = 6, the output should be
numberOfClans(divisors, k) = 4.

The numbers 1 and 5 are friends and form a clan, 
2 and 4 are friends and form a clan, 
and 3 and 6 do not have friends and each is a clan by itself. 
So the numbers 1 through 6 are broken into 4 clans.
'''
