def find(arr, i):
    l = 0
    r = len(arr) - 1
    while l <=r:
        m = (l+r)//2
        if i == arr[m]: return m + 1
        elif i < arr[m]:
            r = m - 1
        else:
            l = m + 1

    return -1


def main():
    _n, *arr1 = map(int, input().split())
    _k, *arr2 = map(int, input().split())
    for i in arr2:
        print(find(arr1, i), end=' ')

if __name__== "__main__":
    main()