import sys, heapq
from collections import defaultdict

dic = defaultdict(int)
n = int(sys.stdin.readline())
q = []

for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    heapq.heappush(q,[-p,d])

ans = 0
while q:
    tmp = heapq.heappop(q)
    if not dic[tmp[1]]:
        ans -= tmp[0]
        dic[tmp[1]] = 1

print(ans)