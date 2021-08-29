import sys

n, m = map(int, sys.stdin.readline().split())
sector = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = int(sys.stdin.readline())

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = sector[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for i in range(k):
    y1,x1,y2,x2 = map(int, sys.stdin.readline().split())
    print(dp[y2][x2] - (dp[y2][x1-1]+dp[y1-1][x2]-dp[y1-1][x1-1]))