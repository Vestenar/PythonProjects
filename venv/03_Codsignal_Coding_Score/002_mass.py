# нарисовать массив 1, n , 2, n-1 ......
def mass(n):
    ans = []
    for i in range(1, (n + 1) // 2 + 1):
        ans.append(i)
        if i < n + 1 - i:
            ans.append(n + 1 - i)

    return ans


task = 7
print(mass(task))
