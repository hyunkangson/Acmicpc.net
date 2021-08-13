""""
문제의 요구사항은 네자리 숫자를 하나씩 바꾸어 정답을 찾아내는 최소 횟수를 구하는 것이다.
처음에 dijkstra하다 잘 해결이 안돼서 bfs로 풀다 문제점을 찾아 다시 dijkstra로도 해결하였다.
"""
#1. bfs code

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



#2. dijkstra code

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
                if 0 <= node + move <= 9999 and eratos[node + move]:
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


"""
이동에 있어 엣지를 타고 가거나 좌표 평면을 이동하거나 하진 않는다.
각 자릿수에 있어 +하거나 -를 하는 값을 저장하여 이를 바탕으로 리스트를 이동한다.

에러를 발생시켰던 사항은 시작 값과 끝나는 값의 범위에서만 이동해서 발생하였다.
기존의 좌표평면 이동과 달리 1000~9999 사이라면 어디든 이동할 수 있다는 점을 간과하여 조건에서 벗어나는 값이 나오면 처리하지 않고 소수도 처리하지 않아서 이 점을 해결하였다.
그리고 a->b로 가는 방법과 b->a로 가는 방법이 같아야 하기에  a > b 라면 b=a, a=b가 되도록 처리하였다.
"""

"""
아무래도 테스트 케이스가 적다 보니 잘못을 고치는 데 어려움이 있어 원문을 찾아 테스트 케이스를 구했다.
<NWERC2006 Problem G: Prime Path>
https://www.csc.kth.se/contest/nwerc/2006/
"""

"""
TestCase
input:
13
1231 1231
1231 1237
1277 9001
9001 8087
8263 9391
9011 8263
7433 4133
3797 3467
8017 1373
3391 8017
1109 1019
9173 1973
2441 9199
output:
0
1
5
4
6
6
3
2
7
5
2
2
8
"""