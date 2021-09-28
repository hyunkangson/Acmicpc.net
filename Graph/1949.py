import sys

def dfs(v):
    visit[v] = 1
    dp[v][0] = nums[v]
    for i in graph[v]:
        if not visit[i]:
            dfs(i)
            dp[v][0] += dp[i][1]
            dp[v][1] += max(dp[i][0], dp[i][1])


n = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0]*2 for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
dfs(1)

print(max(dp[1][0],dp[1][1]))