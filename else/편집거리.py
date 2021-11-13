import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

graph = [[0]*(len(a)+1) for _ in range(len(b)+1)]
graph[0] = [int(i) for i in range(len(a)+1)]
for i in range(len(b)+1):
    graph[i][0] = i

for j in range(1,len(a)+1):
    for i in range(1,len(b)+1):
        if b[i-1] == a[j-1]:
            graph[i][j] = graph[i-1][j-1]
        else:
            graph[i][j] = min(graph[i-1][j],graph[i][j-1],graph[i-1][j-1]) + 1

print(graph[-1][-1])
