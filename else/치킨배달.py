import sys
from itertools import combinations

n,m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

chicken = []; house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i,j])
        if graph[i][j] == 2:
            chicken.append([i,j])

ans = int(1e9)
for c in combinations(chicken,m):
    dist = 0
    for h in house:
        tmp = int(1e9)
        for i in range(m):
            tmp = min(tmp, abs(h[0]-chicken[i][0])+abs(h[1]-chicken[i][1]))
        dist += tmp
    ans = min(ans, dist)

print(ans)