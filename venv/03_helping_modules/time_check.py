import time
start_time = time.time()

a = [11 for i in range(10000)]

print("--- %s seconds ---" % (time.time() - start_time))