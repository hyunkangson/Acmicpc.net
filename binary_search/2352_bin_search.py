from sys import stdin

def search(i):
    st = 0
    ed = len(lines)-1

    while st <= ed:
        mid = (st+ed)//2

        if lines[mid] < i:
            st = mid + 1
        else:
            ed = mid - 1

    return st


n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
lines = []

for i in nums:
    if not lines or lines[-1] < i:
        lines.append(i)
    else:
        lines[search(i)] = i

print(len(lines))