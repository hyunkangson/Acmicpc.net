import sys
from collections import defaultdict


def find(n):
    if p[n] == n:
        return n
    else:
        p[n] = find(p[n])
        return p[n]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        p[y] = x


n = int(sys.stdin.readline())
wi = [int(sys.stdin.readline()) for _ in range(n)]
check = defaultdict(int)
p = [int(i) for i in range(n + 1)]
edges = []

for i in range(n):
    weight = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if weight[j] and not check[(i, j)]:
            check[(i, j)] = 1
            check[(j, i)] = 1
            edges.append([i, j, weight[j]])
for i in range(n):
    edges.append([i, n, wi[i]])
edges.sort(key=lambda x: x[2])

cnt = 0
cost = 0
while edges:
    a, b, w = edges.pop(0)
    if find(a) == find(b):
        continue
    union(a, b)
    cost += w

print(cost)
