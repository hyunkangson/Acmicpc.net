import sys, heapq
inf = int(1e9)

def make(node):
    x = list(map(int, list(str(node))))
    y = [[] for _ in range(4)]
    for i in range(0, 10):
        y[0].append((i - x[0]) * 1000)
        y[1].append((i - x[1]) * 100)
        y[2].append((i - x[2]) * 10)
        y[3].append(i - x[3])
    y[0].pop(0)

    merged = []
    for i in y:
        for j in i:
            merged.append(j)

    return merged


def eratos_sieve():
    eratos = [1] * 10001
    for i in range(2, 10001):
        if eratos[i]:
            for j in range(2 * i, 10001, i):
                eratos[j] = 0

    return eratos


def dijkstra(st, end):
    queue = []
    heapq.heappush(queue, (0, st))
    distance[st] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] >= dist:
            merged = make(node)
            for move in merged:
                if eratos[node + move]:
                    cost = dist + 1
                    if cost < distance[node + move]:
                        distance[node + move] = cost
                        heapq.heappush(queue, (cost, node + move))


n = int(sys.stdin.readline())
nums = []
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
distance = [inf] * 10001

eratos = eratos_sieve()

for a, b in nums:
    if a == b:
        print(0)
        continue
    elif a > b:
        tmp = b
        b = a
        a = tmp

    dijkstra(a, b)

    if distance[b] == inf:
        print("Impossible")
    else:
        print(distance[b])

    distance = [inf] * (10001)