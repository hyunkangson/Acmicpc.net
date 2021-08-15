import sys, heapq

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


q = []
n, m = map(int, sys.stdin.readline().split())
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(q, [c,a,b])

parent = [int(i) for i in range(n+1)]

ans = []
cnt = 0
while q:
    c, a, b = heapq.heappop(q)

    if find(a) == find(b):
        continue
    union(a, b)

    ans.append(c)
    cnt += 1

    if cnt == n - 1:
        break

print(sum(ans) - max(ans))
