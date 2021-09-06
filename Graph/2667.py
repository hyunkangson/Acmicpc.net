import sys
from collections import deque

def bfs(i,j):
    dimension = 1
    q = deque()
    q.append([j,i])

    while q:
        x,y = q.popleft()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append([nx,ny])
                    dimension += 1

    return dimension


n = int(sys.stdin.readline())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
max_val = 0

cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            ans.append(bfs(i,j))
            cnt += 1

ans.sort()

print(cnt)
[print(i) for i in ans]