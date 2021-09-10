import sys,heapq
input = sys.stdin.readline

def dijkstra(st, dest):
    q = []
    heapq.heappush(q,[0,st])
    distance[st] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] >= dist:
            for i in graph[node]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,[cost, i[0]])

    if distance[dest] == int(1e9):
        return False
    return True


n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    tmp = list(input().split())
    for j in range(len(tmp)):
        if tmp[j] == "0":
            continue
        graph[i].append([int(j)+1,1])
        graph[int(j)+1].append([i,1])

itinerary = list(map(int, input().split()))
distance = [int(1e9)] * (n+1)

for i in range(m-1):
    if not dijkstra(itinerary[i], itinerary[i + 1]):
        print("NO")
        exit()
    distance = [int(1e9)] * (n + 1)

print("YES")