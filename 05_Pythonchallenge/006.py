import pickle

i = 0
a = " "
with open("peak.txt", "rb") as f:
    data = pickle.load(f)
print(data)
for ls in data:
    for ch,n in ls:
        print(ch*n,end="")
    print()