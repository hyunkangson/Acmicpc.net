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

"""
DFS 문제로 분류되어있으나 각 엣지가 가중치를 가지기에 다익스트라로 접근했다.
그리고 문제에서 요구하는 사항이 depth에 따른 노드의 level이 아닌 weight에 따른 distance이기에 더 적합한 것 같다.
루트 노드는 항상 1이기에 여기서 가장 먼 노드를 찾으면 지름의 한 끝점이 되고 가장 긴 지름을 원하기에 여기서 가장 먼 노드를 찾으면 다른 끝점이 나와 원하는 답이 된다.

제출 시 오답이 나와 조금 헤매었는데 입력을 다시 보니 2 <= n 이 아닌 1 <= n여서 0의 입력에 대한 처리를 추가해 해결하였다.
"""

