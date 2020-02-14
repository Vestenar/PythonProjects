def checker(line):
    oc = [('(', ')'), ('[', ']'), ('{', '}')]
    opening = [o[0] for o in oc]
    closing = [c[1] for c in oc]
    stack = []
    index = 0
    for ch in line:
        index += 1
        if ch in opening:
            stack.append((ch, index))
        elif ch in closing:
            if len(stack) > 0:
                if closing.index(ch) == opening.index(stack[-1][0]):
                    stack.pop()
                else:
                    print(index)
                    return
            else:
                print(index)
                return
    if len(stack) == 0:
        print('Success')
    else:
        print(stack[-1][1])
    return


def main():
    s = input()
    checker(s)


if __name__ == '__main__':
    main()