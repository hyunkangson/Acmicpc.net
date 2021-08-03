import sys

sys.setrecursionlimit(10000000)


def prt_ans():
    for i in range(1, v + 1):
        for j in graph[i]:
            if visit[i][1] == visit[j][1]:
                return "NO"
    return "YES"


def dfs(vertex):
    visit[vertex][0] = 1
    for i in graph[vertex]:
        if visit[i][0] == 0:
            visit[i][1] = not visit[vertex][1]
            dfs(i)


k = int(sys.stdin.readline())
graph = []
visit = []

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    visit = [[0] * 2 for _ in range(v + 1)]

    for _ in range(e):
        fr, to = map(int, sys.stdin.readline().split())
        graph[fr].append(to)
        graph[to].append(fr)

    for i in range(1, v + 1):
        if visit[i][0] == 0:
            visit[i][1] = True
            dfs(i)

    print(prt_ans())
