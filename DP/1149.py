import sys

n = int(sys.stdin.readline())
dp = [[0] * n for _ in range(3)]

for i in range(n):
    for idx, val in enumerate(map(int, sys.stdin.readline().split())):
        dp[idx][i] = val

print(dp)

for i in range(1, n):
    dp[0][i] += min(dp[1][i - 1], dp[2][i - 1])
    dp[1][i] += min(dp[2][i - 1], dp[0][i - 1])
    dp[2][i] += min(dp[1][i - 1], dp[0][i - 1])

print(dp)
print(min(dp[0][-1], dp[1][-1], dp[2][-1]))