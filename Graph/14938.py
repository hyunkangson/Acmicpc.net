import sys,heapq

def dijkstra(st):
    q = []
    heapq.heappush(q, [0,st])
    distance[st] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] >= dist:
            for v in graph[node]:
                cost = dist + v[1]
                if cost < distance[v[0]]:
                    distance[v[0]] = cost
                    heapq.heappush(q,[cost,v[0]])


n,m,r = map(int, sys.stdin.readline().split())
items = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
distance = [int(1e9)] * (n+1)
for _ in range(r):
    a,b,l = map(int, sys.stdin.readline().split())
    graph[a].append([b,l])
    graph[b].append([a,l])

ans = 0
for i in range(1,n+1):
    dijkstra(i)
    tmp = 0
    for j in range(1,n+1):
        if distance[j] <= m:
            tmp += items[j]

    if ans < tmp:
        ans = tmp

    distance = [int(1e9)] * (n + 1)

print(ans)