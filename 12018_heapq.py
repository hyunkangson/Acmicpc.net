import sys, heapq

n, m = map(int, sys.stdin.readline().split())
q = []

for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    mil = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(mil)
    for _ in range(len(mil)-l):
        heapq.heappop(mil)
    heapq.heappush(q, [len(mil)-l, mil, l])

cnt = 0
for _ in range(len(q)):
    tmp = heapq.heappop(q)
    if tmp[2] > len(tmp[1]):
        m -= 1
        if m < 0:
            break
        cnt += 1
    else:
        m -= heapq.heappop(tmp[1])
        if m < 0:
            break
        cnt += 1

print(cnt)
