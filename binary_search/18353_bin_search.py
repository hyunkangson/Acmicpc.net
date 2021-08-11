from sys import stdin

def search(i):
    st = 0
    ed = len(order) - 1

    while st <= ed:
        mid = (st+ed)//2

        if order[mid] > i:
            st = mid + 1
        else:
            ed = mid - 1

    return st


n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
order = []

for i in nums:
    if not order or order[-1] > i:
        order.append(i)
    else:
        order[search(i)] = i

print(n - len(order))
