

indata = [int(i) for i in input().split()]

if len(indata) > 1:
        if sum(indata) % 2 != 0 and len(indata) % 2 == 0 or indata[0] != indata[1] and len(indata) == 2:
            print('Кучки нельзя уравнять')
        else:
            s = len(indata) * max(indata)
            if (s - sum(indata)) % 2 == 0:
                print(s // 2, max(indata))
            else:
                s += max(indata)
                print(s // 2, max(indata) + 1)
else:
    print('Ошибка. Кучек слишком мало, чтобы можно было решить задачу.')
