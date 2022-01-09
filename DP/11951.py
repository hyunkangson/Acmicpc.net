import sys

n,m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
prefix = [0] * (n+1)

for _ in range(m):
    a,b,k = map(int, sys.stdin.readline().split())
    prefix[a-1] += k
    prefix[b] -= k

for i in range(1, n+1):
    prefix[i] += prefix[i-1]
    h[i-1] += prefix[i-1]

print(*h)
