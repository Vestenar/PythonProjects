import time
from random import random
start_time = time.time()

a = [int(random()*1000) for i in range(10**7)]
b = [i for i in a if i % 10 == 0]
count = 0
for i in b: count += 1
print("--- %s seconds ---" % (time.time() - start_time))
print(count)
