import time
start_time = time.time()
with open(r"c:\adb\dataset_24465_4.txt", "r") as file, open(r"c:\adb\dataset_24465_4_copy.txt","w") as copy:
    f = file.read().splitlines()
    f.reverse()
    for i in f:
        copy.write(i+"\n")
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
with open(r"c:\adb\dataset_24465_4.txt", 'r') as inf, open(r"c:\adb\dataset_24465_4_copy2.txt", 'w') as ouf:
    ouf.write('\n'.join([i for i in reversed(inf.read().splitlines())]))
print("--- %s seconds ---" % (time.time() - start_time))

