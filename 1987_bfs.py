import sys,copy
from collections import deque
def bfs():
    q = deque()
    q.append([0, 0, [graph[0][0]]])
    max_len = 1

    while q:
        x, y, visit = q.popleft()
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nx,ny = x+dx,y+dy
            if 0 <= nx < c and 0 <= ny < r:
                if graph[ny][nx] not in visit:
                    tmp = copy.deepcopy(visit)
                    tmp.append(graph[ny][nx])
                    q.append([nx,ny,tmp])
                    if max_len < len(tmp):
                        max_len = len(tmp)
    return max_len

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(r)]
print(bfs())