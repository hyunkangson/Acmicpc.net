import sys,heapq

maxq = []
minq = []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(minq) == len(maxq):
        heapq.heappush(maxq, -num)
    else:
        heapq.heappush(minq, num)

    if  minq and minq[0] < -maxq[0]:
        tmp = heapq.heappop(minq)
        tmp2 = -heapq.heappop(maxq)
        heapq.heappush(maxq, -tmp)
        heapq.heappush(minq, tmp2)

    print(-maxq[0])
