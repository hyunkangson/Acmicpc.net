import sys, heapq

q = []
n = int(sys.stdin.readline())
for _ in range(n):
    P,Q = map(int, sys.stdin.readline().split())
    heapq.heappush(q, [P,Q])

cnt = 0
com = [0] * n
num = [0] * n
while q:
    tmp = heapq.heappop(q)

    for i in range(len(com)):
        if com[i] <= tmp[0]:
            if com[i] == 0:
                cnt += 1
            com[i] = tmp[1]
            num[i] += 1
            break

print(cnt)

for i in num:
    if i:
        print(i,end= " ")