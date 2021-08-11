import sys,heapq
from collections import defaultdict

def garbage(q):
    while q and visit[q[0][1]] == 0:
        heapq.heappop(q)


for _ in range(int(sys.stdin.readline())):
    minq = []
    maxq = []
    visit = [0] * 1000000

    for i in range(int(sys.stdin.readline())):
        cmd, num = sys.stdin.readline().split()

        if cmd == "I":
            heapq.heappush(minq, (int(num),i))
            heapq.heappush(maxq, (-int(num),i))
            visit[i] = 1
        else:
            if int(num) == 1:
                garbage(maxq)
                if maxq:
                    visit[maxq[0][1]] = 0
                    heapq.heappop(maxq)
            else:
                garbage(minq)
                if minq:
                    visit[minq[0][1]] = 0
                    heapq.heappop(minq)

    garbage(minq)
    garbage(maxq)

    if maxq:
        print(-maxq[0][0], minq[0][0])
    else:
        print("EMPTY")