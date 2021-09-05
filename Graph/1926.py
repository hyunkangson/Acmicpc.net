import sys
from collections import deque

def bfs(i,j):
    global max_val
    dimension = 1
    q = deque()
    q.append([j,i])

    while q:
        x,y = q.popleft()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append([nx,ny])
                    dimension += 1

    if dimension > max_val:
        max_val = dimension


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
max_val = 0

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i,j)
            cnt += 1

print(cnt)
print(max_val)