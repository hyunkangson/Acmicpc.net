import sys
from collections import defaultdict

def find(n):
    if p[n] == n: return n
    else:
        p[n] = find(p[n])
        return p[n]

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y: p[y]=x


n = int(sys.stdin.readline())
planet = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
weight = []
dic = defaultdict(int)

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if dic[(i,j)] == 1:
            continue

        inf = int(1e9)
        tmp = [inf, inf, inf]

        for k in range(3):
            if abs(planet[i][k] - planet[j][k]) < tmp[2]:
                tmp = [i,j,abs(planet[i][k] - planet[j][k])]
        weight.append(tmp)

        dic[(tmp[0],tmp[1])] = 1
        dic[(tmp[1],tmp[0])] = 1

print(weight)
weight = list((sorted(weight, key=lambda x:x[2])))

p = [int(i) for i in range(n)]
cnt = 0; cost = 0
while weight:
    a,b,w = weight.pop(0)
    if find(a) == find(b):
        continue
    cost += w
    union(a,b)
    cnt += 1

    if cnt == n:
        break

print(cost)

