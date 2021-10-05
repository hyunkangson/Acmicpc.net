import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph,n):
    visit = [[int(1e9)]*n for _ in range(n)]
    q = deque()
    q.append([0,0])
    visit[0][0] = graph[0][0]

    while q:
        x, y = q.popleft()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                cost = graph[ny][nx] + visit[y][x]
                if visit[ny][nx] > cost:
                    visit[ny][nx] = cost
                    q.append([nx,ny])

    print(visit[-1][-1])


for _ in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visit = [0]*n
    bfs(graph,n)
