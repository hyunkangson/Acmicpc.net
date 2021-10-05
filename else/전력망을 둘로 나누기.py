from collections import defaultdict
import heapq

def solution(n, wires):
    answer = int(1e9)
    parent = [int(i) for i in range(n + 1)]

    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]

    def union(x,y):
        x = find(x)
        y = find(y)
        if x!=y:
            parent[y] = x

    for i in range(n-1):
        parent = [int(i) for i in range(n + 1)]
        cnt = defaultdict(int)

        for _ in range(2):
            for j in range(n-1):
                if i == j:
                    continue
                if find(wires[j][0]) == find(wires[j][1]):
                    continue
                union(wires[j][0],wires[j][1])

        for k in range(1,n+1):
            cnt[parent[k]] += 1

        cnt = list(cnt.values())

        if len(cnt) == 2:
            if abs(cnt[0]-cnt[1]) < answer:
                answer = abs(cnt[0]-cnt[1])

    return answer

print(solution(7,	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	))