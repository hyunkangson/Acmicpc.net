import sys, heapq

def print_(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1][0:len(nums[i])]:
            return "NO"
    return "YES"


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    nums = [sys.stdin.readline().rstrip() for _ in range(n)]
    print(print_(sorted(nums)))