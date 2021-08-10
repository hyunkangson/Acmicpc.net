import sys, heapq

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    heapq.heappush(q,[a,b])
target, fuel = map(int, sys.stdin.readline().split())

cnt = 0
bucket = []
while fuel < target:
    while q and q[0][0] <= fuel:
        tmp = heapq.heappop(q)
        heapq.heappush(bucket, [-tmp[1], tmp[0]])

    if not bucket:
        cnt = -1
        break

    tmp = heapq.heappop(bucket)
    fuel -= tmp[0]
    cnt += 1

print(cnt)