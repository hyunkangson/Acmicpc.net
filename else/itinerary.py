import sys

def find(x):
    if parent[x] == x:
        return parent[x]
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x,y):
    x = find(parent[x])
    y = find(parent[y])
    if x != y:
        parent[y] = x


n,m = map(int, sys.stdin.readline().split())
parent = [int(i) for i in range(n+1)]

for i in range(n):
    graph = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if graph[j] == 1:
            union(i,j)
