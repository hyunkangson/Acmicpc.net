import sys

def search(nums):
    global cnt
    st = 0
    ed = n-1
    while st < ed:
        tmp = nums[st]+nums[ed]
        if abs(tmp) < cnt[0]:
            cnt = [abs(tmp), nums[st], nums[ed]]

        if tmp < 0:
            st += 1
        else:
            ed -= 1


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
cnt = [sys.maxsize,0,0]
search(sorted(nums))
print(cnt[1], cnt[2])