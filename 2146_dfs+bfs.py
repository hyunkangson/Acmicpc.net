import sys
from collections import deque

def bfs(z):
    global ans
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if graph[ny][nx] > 0 and graph[ny][nx] != z:
                ans = min(ans, dist[y][x])
                return
            if graph[ny][nx] == 0 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append([ny, nx])


def filling(y, x):
    global cnt
    check[y][x] = 1
    graph[y][x] = cnt

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if check[ny][nx] == 0 and graph[ny][nx]:
            filling(ny, nx)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
ans = sys.maxsize
cnt = 1

for i in range(n):
    for j in range(n):
        if check[i][j] == False and graph[i][j] == 1:
            filling(i, j)
            cnt += 1

for i in range(1, cnt):
    bfs(i)

print(ans)