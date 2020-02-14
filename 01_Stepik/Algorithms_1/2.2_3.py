def fib_mod(n,m):
    arr = [0, 1]
    if n ==1:
        return arr[n % len(arr)]
    
    for i in range(2, m*6 +1):
        arr.append((arr[i-1] + arr[i-2]) % m)
        if arr[i] == 1 and arr[i-1] == 0:
            break
    print(arr[:-2])
    return arr[n % (len(arr) - 2)]




def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))

if __name__ == "__main__":
    main()

#  139583862445 --55e