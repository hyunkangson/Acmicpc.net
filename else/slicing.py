from sys import stdin

def search():
    ed = max(nums)
    st = 0

    while st <= ed:
        mid = (st+ed)//2

        summation = 0
        for n in nums:
            if n - mid > 0:
                summation += n - mid

        if summation < m:
            ed = mid - 1
        else:
            st = mid + 1

    return ed


_, m = map(int, stdin.readline().split())
nums = list(map(int,stdin.readline().split()))

print(search())
