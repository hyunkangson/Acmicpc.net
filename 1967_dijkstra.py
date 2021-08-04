import sys
import heapq
inf = int(1e9)

def dijkstra(st):
    queue = []
    heapq.heappush(queue, (0, st))
    distance[st] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for v in graph[node]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(queue, (cost, v[0]))

    return max(distance)

n = int(sys.stdin.readline())
if n == 1:
    print(0)
    exit()

graph = [[] for _ in range(n+1)]
distance = [0] + [inf] * n

for _ in range(n-1):
    fr, to, weight = map(int, sys.stdin.readline().split())
    graph[fr].append([to,weight])
    graph[to].append([fr,weight])

dijkstra(1)
st = distance.index(max(distance))
distance = [0] + [inf] * n
print(dijkstra(st))