import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
    nums.sort()
    print(nums[(len(nums)-1)//2])
