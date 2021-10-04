import sys

n = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

ans = 0
distance = 0
cnt = cost[0]

for i in range(1,n):
    distance += dist[i-1]
    if cnt > cost[i]:
       ans += distance*cnt
       distance = 0
       cnt = cost[i]

if distance:
    ans += distance * cnt

print(ans)
