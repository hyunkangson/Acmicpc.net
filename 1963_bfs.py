import sys
from collections import deque

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
    eratos = [1] * (10001)
    for i in range(2, 10001):
        if eratos[i]:
            for j in range(2 * i, 10001, i):
                eratos[j] = 0

    return eratos


def bfs(st,end):
    q = deque()
    q.append((0, st))
    visit = [0]*10001
    visit[st] = 1

    while q:
        dist, node = q.popleft()
        if node == end:
            ans.append(dist)
        merged = make(node)
        for move in merged:
            newnode = node + move
            if 1000 <= newnode <= 9999 and eratos[newnode]:
                if visit[newnode] == 0:
                    visit[newnode] = 1
                    q.append((dist+1,newnode))


n = int(sys.stdin.readline())
nums = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
eratos = eratos_sieve()
ans = []

for a,b in nums:
    if a == b:
        print(0)
        continue
    elif a > b:
        tmp = b
        b = a
        a = tmp

    bfs(a,b)
    if ans:
        print(ans[-1])
    else:
        print("Impossible")


