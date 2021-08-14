import sys


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

st = 0
ed = max(nums)

while st <= ed:
    mid = (st+ed)//2
    cnt = 0
    for i in nums:
        if i > mid:
            cnt += mid
        else:
            cnt += i

    if cnt > m:
        ed = mid -1
    else:
        st = mid + 1

print(ed)