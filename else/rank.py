import sys

n,m = map(int, sys.stdin.readline().split())
inf = int(1e9)
dist = [[inf] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    x,y = map(int, input().split())
    dist[x][y] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if j == k:
                continue
            if dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

ans = 0

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if dist[i][j] != inf and dist[i][j] != 0:
            cnt += 1
        if dist[j][i] != inf and dist[j][i] != 0:
            cnt += 1
    if cnt == n-1:
        ans += 1

print(ans)