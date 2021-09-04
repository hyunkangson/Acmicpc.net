import sys,heapq

def dijkstra(st):
    q = []
    heapq.heappush(q,[st,0])
    distance[st] = 0

    while q:
        node, dist = heapq.heappop(q)
        for i in graph[node]:
            cost = dist + 1
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q, [i,cost])


n,m,k,x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [int(1e9)] * (n+1)

for _ in range(m):
    a,b = map(int , sys.stdin.readline().split())
    graph[a].append(b)

dijkstra(x)

ans = []
for i in range(1,n+1):
    if distance[i] == k:
        ans.append(i)

if ans:
    for i in ans:
        print(i)
else:
    print(-1)