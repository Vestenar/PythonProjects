def countSumOfTwoRepresentations2(n, l, r):
    return sum(1 for a in range(l, r + 1) if l <= a <= n - a <= r)

print(countSumOfTwoRepresentations2(93,24,58))


assert countSumOfTwoRepresentations2(6,2,4) == 2, "1"
assert countSumOfTwoRepresentations2(6,3,3) == 1, "2"
assert countSumOfTwoRepresentations2(10,9,11) == 0, "3"
assert countSumOfTwoRepresentations2(24,8,16) == 5, "4"
assert countSumOfTwoRepresentations2(24,12,12) == 1, "5"
assert countSumOfTwoRepresentations2(93,24,58) == 12, "6"
print("well done")

'''
Given integers n, l and r, find the number of ways to
represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2, and r = 4, the output should be
countSumOfTwoRepresentations2(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.
'''
