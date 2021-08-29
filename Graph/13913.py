from collections import deque
import sys

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            break
        for y in x-1, x+1, x*2:
            if 0 <= y <= 100000 and visit[y] == -1:
                q.append(y)
                visit[y] = x


n, k = list(map(int, input().split()))
visit = [-1] * 100001
visit[n] = -2

bfs()

ans = []
while k != -2:
    ans.append(k)
    k = visit[k]

ans.reverse()
print(len(ans)-1)
print(' '.join(map(str, ans)))