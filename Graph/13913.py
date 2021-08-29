import sys
from collections import deque,defaultdict

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            return
        for y in x-1, x+1, x*2:
            if 0 <= y <= k and route[y] == 0:
                route[y] = x
                q.append(y)


n, k = map(int, sys.stdin.readline().split())
route = defaultdict(int)
bfs()
ans = [k]
while n != k:
    ans.insert(0, route[k])
    k = route[k]

print(len(ans)-1)
print(*ans)