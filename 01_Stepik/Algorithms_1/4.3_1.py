import heapq

def main():
    hp = []
    n = int(input())
    for _ in range(n):
        cmd = input().strip()
        if cmd == "ExtractMax":
            a = heapq.heappop(hp) * -1
            print(a)
        else:
            val = int(cmd.split()[1]) * -1
            heapq.heappush(hp, val)


if __name__ == "__main__":
    main()
