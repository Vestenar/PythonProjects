def stairs(arr):
    s = [0, 0]
    for i in arr:
        s.append(max(i + s[-1], i + s[-2]))
    return s[-1]

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(stairs(arr))


def test():
    assert -63 == stairs([-2, -16, -13, -9, -48])
    assert 2 == stairs([1, 1, -2, -4, -6, 2, 2])
    assert -73 == stairs([-64, -16, -13, -9, -48])
    assert 5 == stairs([0, 0, 0, 4, 6, -5])
    assert -9 == stairs([-6, 4, -16, -13, -9, 0])
    assert -18 == stairs([-6, 4, -16, -13, -9])
    assert 21 == stairs([3, 4, 10, 10, 0, -6, -10, 0])
    assert 3 == stairs([1, 2])
    assert 1 == stairs([2, -1])
    assert 3 == stairs([-1, 2, 1])
    assert 2 == stairs([2])
    assert -2 == stairs([-2])


if __name__ == "__main__":
    main()
    test()