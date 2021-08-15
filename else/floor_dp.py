import sys

n = int(sys.stdin.readline())
dp = [0,1,3] + [0] * 999
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n] % 796796)