import sys,heapq

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    nums = sorted(list(map(int, sys.stdin.readline().split())))
    costs = 1
    heapq.heapify(nums)

    while len(nums) > 1:
        a, b = heapq.heappop(nums), heapq.heappop(nums)
        costs *= a*b
        heapq.heappush(nums,a*b)

    print(costs%(1000000007))