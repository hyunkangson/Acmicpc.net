import sys, heapq

q = []
n = int(sys.stdin.readline())
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in tmp:
        heapq.heappush(q,j)
        if len(q) > n:
            heapq.heappop(q)
print(heapq.heappop(q))