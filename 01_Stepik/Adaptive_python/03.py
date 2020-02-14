# n = int(input())
# arr = []
# i = 1
# while len(arr) <= n:
#     arr += [i] * i
#     i += 1
# arr = arr[:n]
# for i in arr:
#     print(i, end=" ")

def gen():
    i = 0
    while True:
        i += 1
        for _ in range(i):
            yield i

a = gen()
for j in range(int(input())):
    print(next(a), end=' ')