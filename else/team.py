import sys

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


n,m = map(int, sys.stdin.readline().split())
parent = [int(i) for i in range(n+1)]
print("\n")
for _ in range(m):
    dec, a, b = map(int, sys.stdin.readline().split())
    if dec:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)
