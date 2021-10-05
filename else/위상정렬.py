import sys
from collections import defaultdict

def dfs(st):
    visit[st] = 1
    order.append(st)
    ans[st] += time[st]
    for i in graph[st]:
        if visit[i] == 0:
            visit[i] = 1
            ans[i] += ans[st]
            dfs(i)


n = int(sys.stdin.readline())
graph = [[] for  i in range(n+1)]
visit = [0] * (n+1)
ans = [0] * (n+1)
order = []

time = defaultdict(int)
st = 0

for i in range(1, n+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    if len(tmp) == 2:
        st = i
    else:
        for j in range(1,len(tmp)-1):
            graph[tmp[j]].append(i)
    time[i] = tmp[0]

dfs(st)

for i in order:
    print(ans[i])
