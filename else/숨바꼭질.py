import heapq,sys

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 1))
    distance[1] = 0

    while queue:
        dist, vertex = heapq.heappop(queue)
        if distance[vertex] < dist:
            continue
        for v, w in graph[vertex]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))


n, edges = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [0] + [sys.maxsize] * n

for i in range(edges):
    fr, to = map(int, sys.stdin.readline().split())
    graph[fr].append((to, 1))
    graph[to].append((fr, 1))

dijkstra()
x = max(distance)
print(distance.index(x), x, distance.count(x))