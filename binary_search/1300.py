import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
st = 1
ed = k

ans = 0
while st <= ed:
    mid = (st+ed)//2
    tmp = 0
    for i in range(1,n+1):
        tmp += min(mid//i, n)
    if tmp >= k:
        ans = mid
        ed = mid-1
    else:
        st = mid+1

print(ans)