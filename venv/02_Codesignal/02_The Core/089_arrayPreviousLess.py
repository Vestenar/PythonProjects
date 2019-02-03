def arrayPreviousLess(items):
    ans = []
    for i in range(len(items)):
        temp = -1
        for j in range(i-1, -1, -1):
            if items[i] > items[j]:
                temp = items[j]
                break
        ans.append(temp)
    return ans


items = [2, 2, 1, 3, 4, 5, 5, 3]
print(arrayPreviousLess(items))
'''
# нужно вставить самое правое из чисел слева, которое меньше, чем текущее!

Given array of integers, for each position i, search among the previous positions 
for the last (from the left) position that contains a smaller value. 
Store this value at position i in the answer. If no such value can be found, store -1 instead.

Example

For items = [3, 5, 2, 4, 5], the output should be
arrayPreviousLess(items) = [-1, 3, -1, 2, 4].
'''