import sys,heapq

nums = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(nums,-x)
    else:
        if nums:
            print(abs(heapq.heappop(nums)))
        else:
            print(0)
