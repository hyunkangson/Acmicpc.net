import sys
sys.setrecursionlimit(int(1e9))

def dfs(i,j):
    global cnt
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for k in range(4):
        nx,ny = j + dx[k], i + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[ny][nx] == 0 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                cnt += 1
                dfs(ny,nx)


m,n,k = map(int, sys.stdin.readline().split())

graph = [[0]*n for _ in range(m)]
visit = [[0]*n for _ in range(m)]

for _ in range(k):
    coord = list(map(int, sys.stdin.readline().split()))
    for i in range(coord[1],coord[3]):
        for j in range(coord[0],coord[2]):
            graph[i][j] = 1

ans = 0
ans2 = []
cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visit[i][j] == 0:
            ans += 1
            visit[i][j] = 1
            cnt = 1
            dfs(i,j)
            ans2.append(cnt)

print(ans)
print(" ".join(str(i) for i in sorted(ans2)))