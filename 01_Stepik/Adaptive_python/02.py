arr = [int(x) for x in input().split()]
n = int(input())
if n not in arr:
    print("None")
else:
    ans = [str(i) for i in range(len(arr)) if arr[i] == n]
    print(" ".join(ans))