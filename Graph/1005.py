from collections import deque
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n,k = map(int, sys.stdin.readline().split()) # n:건물의 개수, k:규칙의 개수
    time = [0] + list(map(int, sys.stdin.readline().split())) # 공백 시간
    graph = [[] for _ in range(n+1)]
    degree = [int(1e9)] + [0]*n

    for _ in range(k):
        x,y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        degree[y] += 1

    w = int(sys.stdin.readline())

    dp = [0] * (n+1)
    q = deque()
    for i in range(1,n+1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        vtx = q.popleft()
        for v in graph[vtx]:
            degree[v] -= 1
            dp[v] = max(dp[v], dp[vtx] + time[v])
            if degree[v] == 0:
                q.append(v)

        if degree[w] == 0:
            print(dp[w])
            break

