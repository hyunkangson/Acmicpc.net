import sys

n,c = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
start = 1
end = nums[-1] - nums[0]

def search(dist):
    count = 1
    cur = nums[0]
    for i in range(1, n):
        if cur + dist <= nums[i]:
            count +=1
            cur = nums[i]
    return count


while start <= end:
    pos = (start + end)//2
    if search(pos) >= c:
        answer = pos
        start = pos +1
    else:
        end = pos - 1

print(answer)