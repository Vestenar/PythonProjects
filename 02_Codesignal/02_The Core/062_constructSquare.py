def constructSquare(s):  # долгое решение
    if len(s) == 0: return -1
    ans, val =- 1, 10
    used, nums = {}, {}
    for ch in s:
        if ch not in used:
            val -= 1
            if val <0: return ans
            used[ch] = s.count(ch)
    sq = int("9"*len(s))
    min = int("1"+"0"*(len(s)-1))**0.5
    sq = int(sq)
    n = int(sq ** 0.5)
    while n >= min:
        ss = n*n
        for ch in str(ss):
            nums[ch] = str(ss).count(ch)
        if sorted(list(used.values())) == sorted(list(nums.values())): return ss
        nums = {}
        n -=1
    return ans

# def constructSquare(s):
#     p = len(s)
#     d_max = int((10**p)**.5)
#     d_min = int((10**(p-1))**.5)
#     for d in range(d_max, d_min-1, -1):
#         n = str(d * d)
#         if sorted(s.count(c) for c in s) == sorted(n.count(c) for c in n):
#             return int(n)
#     return -1


task = "abccccdddd"
# Expected Output: 999950884

print(constructSquare(task))
'''
Given a string consisting of lowercase English letters, find the largest square number 
which can be obtained by reordering the string's characters and replacing them with any digits you need 
(leading zeros are not allowed) where same characters always map to the same digits 
and different characters always map to different digits.

If there is no solution, return -1.

Example

    For s = "ab", the output should be
    constructSquare(s) = 81.
    The largest 2-digit square number with different digits is 81.
    For s = "zzz", the output should be
    constructSquare(s) = -1.
    There are no 3-digit square numbers with identical digits.
    For s = "aba", the output should be
    constructSquare(s) = 900.
    It can be obtained after reordering the initial string into "baa" and replacing "a" with 0 and "b" with 9.

'''
