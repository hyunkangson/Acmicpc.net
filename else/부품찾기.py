import sys
n = int(sys.stdin.readline())
parts = list(map(int,sys.stdin.readline().split()))
parts.sort()
m = int(sys.stdin.readline())
part = list(map(int,sys.stdin.readline().split()))

for p in part:
    cnt = 0
    st = 0
    ed = len(parts)
    while st <= ed:
        mid = (st+ed)//2
        if parts[mid] == p:
            print("yes")
            cnt = 1
            break
        elif parts[mid] > p:
            ed = mid-1
        else:
            st = mid+1
    if cnt == 0:
        print("no")