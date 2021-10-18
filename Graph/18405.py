import sys
from collections import deque

def bfs():
    q = deque()
    q += virus

    while q:
        num,x,y,cnt = q.popleft()
        if cnt == s:
            return graph[a-1][b-1]
        for dx,dy in (0,1),(1,0),(0,-1),(-1,0):
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and not graph[ny][nx]:
                graph[ny][nx] = num
                q.append([num,nx,ny,cnt+1])

    return graph[a-1][b-1]


n,k = map(int ,sys.stdin.readline().split())
graph = []; virus = []
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j]:
            virus.append([tmp[j],j,i,0])
s,a,b = map(int, sys.stdin.readline().split())
virus.sort()

print(bfs())
