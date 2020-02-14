"""
Алгоритм сортировки слиянием.
Дополнительно выводит количество инверсий в исходном списке.
На вход в первой строке подается число n элементов в массиве,
во второй строке непосредственно числа массива, разделенные пробелами.
"""

count = 0
"""
Функция слияния двух массивов. Слияние производится путем сравнения первых элементов массивов,
затем идентификатор ячейки массива сдвигается вправо.
"""
def merge(left, right):
    out_arr = []
    global count
    lid, rid = 0, 0
    while lid < len(left) and rid < len(right):
        if left[lid] <= right[rid]:
            out_arr.append(left[lid])
            lid += 1
        else:
            out_arr.append(right[rid])
            rid += 1
            count += len(left) - lid

    if left:
        out_arr.extend(left[lid:])
    if right:
        out_arr.extend(right[rid:])
    return out_arr

"""
Функция рекурсивного разделения исходного массива на короткие массивы.
Не обязательно делить массив до длины 1, достаточно ограничить некоторым удовлетворяющим числом,
после чего полученный массив следует отсортировать и вернуть.
"""

def mergesort(a):
    if len(a) < 2:          # если выбрано иное число, то в условие следует добавить сортировку
        return a
    m = len(a) // 2
    return merge(mergesort(a[:m]), mergesort(a[m:]))

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    mergesort(a)
    print(count)

if __name__ == "__main__":
    main()


# arr1 = [2,4,8,14]
# arr2 = [0,8,9,11]

# print(merge(arr1,arr2))

# 7 2 5 3 7 13 1 6