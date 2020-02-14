import heapq

n, m = map(int, input().split())
times = list(map(int, input().split()))
procs = [[0, i] for i in range(n)]
heapq.heapify(procs)

for time in times:
    print(procs[0][1], procs[0][0])
    top = heapq.heappop(procs)
    top[0] += time
    heapq.heappush(procs, top)
