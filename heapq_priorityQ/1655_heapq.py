import sys,heapq

maxq = []
minq = []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(minq) == len(maxq):
        heapq.heappush(maxq, [-num,num])
    else:
        heapq.heappush(minq, [num,num])

    if  minq and minq[0][1] < maxq[0][1]:
        tmp = heapq.heappop(minq)[1]
        tmp2 = heapq.heappop(maxq)[1]
        heapq.heappush(maxq, [-tmp, tmp])
        heapq.heappush(minq, [tmp2, tmp2])

    print(maxq[0][1])