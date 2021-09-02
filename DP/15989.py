import sys

dp = [1,1,2,3] + [0] * 9997
for i in range(4, 10001):
    dp[i] = dp[i-1] + (dp[i-2]-dp[i-3])
    if i % 3 == 0:
        dp[i] += 1


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(dp[n])