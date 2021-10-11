import sys
sys.setrecursionlimit(int(1e9))

def dfs(v):
    for w in works[v]:
        if visit[w]:
            continue
        visit[w] = 1
        if done[w] == -1 or dfs(done[w]):
            done[w] = v
            return 1
    return 0


n,m = map(int, sys.stdin.readline().split())
works = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(n)]
done = [-1] * (m + 1)

cnt = 0
for i in range(n):
    visit = [0] * (m+1)
    if dfs(i):
        cnt += 1

print(cnt)