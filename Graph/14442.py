import sys
from collections import deque

def bfs():
    q = deque()
    q.append([0,0,0])
    visit = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
    visit[0][0] = [1] * (k+1)

    while q:
        x,y,z = q.popleft()
        dist = visit[y][x][z]
        if x == m-1 and y == n-1:
            return visit[y][x][z]
        for dx,dy in (0,1), (1,0), (0,-1), (-1,0):
            nx,ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and not visit[ny][nx][z]:
                if graph[ny][nx] == "0":
                    visit[ny][nx][z] = dist + 1
                    q.append([nx,ny,z])
                elif z < k:
                    visit[ny][nx][z+1] = dist + 1
                    q.append([nx,ny,z+1])
    return -1


n,m,k = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
print(bfs())