import sys

n = int(sys.stdin.readline())
t= []; p = []
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

dp = [0] * (n+1)
mx = 0
for i in reversed(range(n)):
    if n - i < t[i]:
        continue

    dp[i] = max(p[i]+dp[t[i]+i], mx)
    mx = dp[i]

print(mx)