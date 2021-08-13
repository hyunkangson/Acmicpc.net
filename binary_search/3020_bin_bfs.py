import sys
from collections import deque

def bfs(w):
    q = deque()
    q.append(ans[0])
    visit = [0] * (n+1)
    visit[ans[0]] = 1

    while q:
        x = q.popleft()
        if x == ans[1]:
            return 1
        for i,j in graph[x]:
            if j >= w and not visit[i]:
                visit[i] = 1
                q.append(i)

    return 0


def search():
    cnt = 1
    st = 1
    ed = 1000000000

    while st <= ed:
        mid = (ed+st)//2
        tmp = bfs(mid)

        if tmp == 1:
            cnt = mid
            st = mid + 1
        else:
            ed = mid - 1

    print(cnt)


n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


ans = list(map(int,sys.stdin.readline().split()))
search()

