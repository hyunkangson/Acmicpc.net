from collections import deque
import sys

def dfs(num,cnt):
    if cnt == n:
        ans[0] = max(ans[0], num)
        ans[1] = min(ans[1], num)
        return

    if oper[0]:
        oper[0] -= 1
        dfs(num+nums[cnt], cnt+1)
        oper[0] += 1

    if oper[1]:
        oper[1] -= 1
        dfs(num-nums[cnt], cnt+1)
        oper[1] += 1

    if oper[2]:
        oper[2] -= 1
        dfs(num*nums[cnt], cnt+1)
        oper[2] += 1

    if oper[3]:
        tmp = abs(num) // nums[cnt]
        if num < 0:
            tmp *= -1
        oper[3] -= 1
        dfs(tmp, cnt+1)
        oper[3] += 1


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))

ans = [ -int(1e9), int(1e9)]
num = nums[0]
dfs(num,1)

print(ans[0])
print(ans[1])