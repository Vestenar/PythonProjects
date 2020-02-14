def spiralNumbers(m):

    mx = [[0 for i in range(m)] for j in range(m)]
    cnt = 1
    for i in range(m):
        mx[0][i] = cnt
        cnt += 1
    n = m - 1
    while cnt < m ** 2:
        for j in range(m // 2):
            for i in range(n):
                mx[i + j + 1][m - j - 1] = cnt
                cnt += 1
            for i in range(n):
                mx[m - j - 1][m - j - i - 2] = cnt
                cnt += 1
            n -= 1
            for i in range(n):
                mx[m - j - i - 2][j] = cnt
                cnt += 1
            for i in range(n):
                mx[j + 1][j + i + 1] = cnt
                cnt += 1
            n -= 1
    return mx




# рекурсионная формула на Py2

# def spiralNumbers(n, m=0, s=1):
#     if m == 0:
#         m = n
#     if n == 1 == m:
#         return [[s]]
#
#    # Calculate spiral numbers without first row
    # S = spiralNumbers(m - 1, n, s + n)
    #
#    # Create first row and add the transpose of the rest
    # return [range(s, s + n)] + zip(*S[::-1])

print(spiralNumbers(5))
