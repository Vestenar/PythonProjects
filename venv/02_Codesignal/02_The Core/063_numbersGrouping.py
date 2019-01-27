def numbersGrouping(a):
    # a.sort()
    # n = 0
    # group = set()
    group = set((el-1)//1e4 for el in a)
    # for el in a:
    #     count = False
    #     while not count:
    #         if n * 1e4 + 1 <= el <= (n + 1) * 1e4:
    #             count = True
    #             group.add(n + 1)
    #         else:
    #             n += 1
    return len(a) + len(group)


ls = [20000, 239, 10001, 999999, 10000, 20566, 29999]
print(numbersGrouping(ls))

ls = [10000, 20000, 30000, 40000, 50000, 60000, 10000, 120000, 150000, 200000, 300000, 1000000, 10000000, 100000000,
      10000000]
print(numbersGrouping(ls))

ls = [10000, 1]
print(numbersGrouping(ls))

'''
You are given an array of integers that you want distribute between several groups. 
The first group should contain numbers from 1 to 104, 
the second should contain those from 104 + 1 to 2 * 104, ..., 
the 100th one should contain numbers from 99 * 104 + 1 to 106 and so on.

All the numbers will then be written down in groups to the text file in such a way that:

    the groups go one after another;
    each non-empty group has a header which occupies one line;
    each number in a group occupies one line.

Calculate how many lines the resulting text file will have.

Example

For a = [20000, 239, 10001, 999999, 10000, 20566, 29999], the output should be
numbersGrouping(a) = 11.
'''
