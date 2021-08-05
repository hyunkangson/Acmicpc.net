import sys,copy
from collections import deque
def bfs():
    q = deque()
    q.append([0,0])
    visit = [[[] for _ in range(c)] for _ in range(r)]
    visit[0][0].append(graph[0][0])
    while q:
        x, y = q.popleft()
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nx,ny = x+dx,y+dy
            if 0 <= nx < c and 0 <= ny < r:
                if len(visit[ny][nx]) < len(visit[y][x])+1 and graph[ny][nx] not in visit[y][x]:
                    tmp = copy.deepcopy(visit[y][x])
                    tmp.append(graph[ny][nx])
                    visit[ny][nx] = tmp
                    q.append((nx,ny))
    return visit

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(r)]
ans = bfs()
max_len = 0

for i in ans:
    for j in i:
        if len(j) > max_len:
            max_len = len(j)
print(max_len)