import sys
from collections import deque

for _ in range(int(stdin.readline())):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    rank = [[0] * (n + 1) for _ in range(n + 1)]
    in_degree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1, n):
            rank[nums[i]][nums[j]] = 1

    m = int(stdin.readline())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        rank[a][b], rank[b][a] = rank[b][a], rank[a][b]

    ans = []
    q = deque()
    for i in range(1, n+1):
        in_degree[i] = rank[i].count(1)
        if in_degree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        ans.append(cur)
        for i in range(1, n+1):
            if rank[i][cur]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)

    if len(ans) == n:
        print(*ans[::-1])
    else:
        print("IMPOSSIBLE")