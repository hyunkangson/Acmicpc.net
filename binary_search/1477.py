import sys

n, m, l = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
nums.insert(0,0)
nums.append(l-1)

st = 0
ed = l - 1
ans = 0
while st <= ed:
    mid = (st+ed)//2
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > mid:
            cnt += (nums[i] - nums[i-1] -1)//mid

    if cnt > m:
        st = mid + 1
    else:
        ans = mid
        ed = mid - 1

print(ans)
