import sys

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


g = int(sys.stdin.readline())
planes = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
parent = [int(i) for i in range(g+1)]

ans = 0
for p in planes:
    n = find(p)
    if not n:
        break
    ans += 1
    union(n-1, n)

print(ans)
