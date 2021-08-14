import sys

def search(i):
    global cnt
    target = nums[i]
    nums.pop(i)
    st = 0
    ed = l - 2

    while st < ed:
        val = nums[st] + nums[ed]
        if  val == target:
            cnt += 1
            break
        elif val < target:
            ed -=1
        else:
            st += 1

    nums.insert(i, target)


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=True)
l = len(nums)
cnt = 0
[search(i) for i in range(l)]

print(cnt)