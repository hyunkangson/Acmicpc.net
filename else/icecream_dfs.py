import sys
sys.setrecursionlimit(int(1e9))

def dfs(i,j):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for k in range(4):
        nx,ny = j+dx[k], i+dy[k]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == "0" and not visit[ny][nx]:
                visit[ny][nx] = 1
                dfs(ny,nx)


n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "0" and not visit[i][j]:
            visit[i][j] = 1
            ans += 1
            cnt = 1
            dfs(i,j)

print(ans)