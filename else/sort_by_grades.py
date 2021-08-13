import sys, heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    heapq.heappush(q, [int(b), a])

for _ in range(n):
    print(heapq.heappop(q)[1], end = " ")