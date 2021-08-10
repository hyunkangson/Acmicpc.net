import sys,heapq

maxq = []
minq = []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(minq) == len(maxq):
        heapq.heappush(minq, [-num,num])
    else:
        heapq.heappush(maxq, [num,num])

    if  maxq and maxq[0][1] < minq[0][1]:
        tmp = heapq.heappop(minq)[1]
        tmp2 = heapq.heappop(maxq)[1]
        heapq.heappush(minq, [-tmp2, tmp2])
        heapq.heappush(maxq, [tmp, tmp])

    print(minq[0][1])
