import time
start_time = time.time()


def count(l):
    n = [0]
    # for i in range(10**l):
    #     n.append(i)
    #     n.pop(0)
    # return n[-1]
    a = int("9"*l)
    b = 10**l
    # for i in range(b):
    #     if i == a:
    #         n.append(i)
    #         n.pop(0)
    n = [i for i in range(b) if i == a]
    return n
print(count(8))
print("--- %s seconds ---" % (time.time() - start_time))
a = input()
