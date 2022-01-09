import sys

def check(x):
    cnt = 0
    cnt2 = 0
    for i in info:
        if i[0] > x:
            return False
        cnt += min(x-i[0], i[1]-i[0]) # 여유분
        cnt2 += i[0] # 최소

    if cnt + cnt2 >= t:
        return True


n, t = map(int, sys.stdin.readline().split())
info = []
l = int(1e9)
r = 0

cnt = [0,0]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    info.append([a, b])
    cnt[0] += a; cnt[1] += b
    r = max(r, b); l = min(l, a)

if cnt[0] > t or cnt[1] < t:
    print(-1)
    exit(0)

while l <= r:
    mid = (l + r) // 2
    if check(mid):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)