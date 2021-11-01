import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
l = 0; r = n-1
while l<r:
    mid = (l+r)//2
    if nums[mid] == mid:
        print(mid)
        exit()
    if nums[mid] > mid:
        r = mid - 1
    else:
        l = mid + 1

print(-1)