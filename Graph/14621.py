import sys,heapq

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


n, m = map(int, sys.stdin.readline().split())
gender = list(map(str, sys.stdin.readline().split()))
gender.insert(0,0)
q = []
for _ in range(m):
    u,v,d = map(int, sys.stdin.readline().split())
    if gender[u] != gender[v]:
        heapq.heappush(q, [d,u,v])

parent = [int(i) for i in range(n+1)]

ans = 0
cnt = 0
while q:
    c, a, b = heapq.heappop(q)

    if find(a) == find(b):
        continue

    union(a,b)

    ans += c
    cnt += 1

    if cnt == n-1:
        break

if cnt != n-1:
    print(-1)
else:
    print(ans)