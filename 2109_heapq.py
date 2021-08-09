import sys, heapq
from collections import defaultdict

def move(day):
    for _ in range(day):
        if day == 0:
            return 0
        if not dic[day]:
            dic[day] = 1
            return day
        else:
            day -= 1
    return 0


dic = defaultdict(int)
n = int(sys.stdin.readline())
q = []

for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    heapq.heappush(q,[-p,d])

ans = 0
while q:
    tmp = heapq.heappop(q)
    if move(tmp[1]):
        ans -= tmp[0]

print(ans)