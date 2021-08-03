import sys
sys.setrecursionlimit(1000000)

def dfs(i,j):
    if dp[i][j]:
        return dp[i][j]

    dp[i][j] = 1
    for dx,dy in (-1,0),(1,0),(0,1),(0,-1):
        nx, ny = i+dx, j+dy
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > graph[i][j]:
                dp[i][j] = max(dp[i][j], dfs(nx, ny) + 1)
    return dp[i][j]

n = int(sys.stdin.readline())
graph =[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

ans = 1
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))

print(ans)

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break