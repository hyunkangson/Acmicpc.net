import sys


def check(n):
    while True:
        cnt = 0
        if n % 5 == 0:
            n /= 5
            cnt += 1
        elif n % 3 == 0:
            n /= 3
            cnt += 1
        elif n % 2 == 0:
            n /= 2
            cnt += 1

        if n == 1:
            return 1
        elif cnt == 0:
            return 0


n = int(sys.stdin.readline())

cnt = 0
for i in range(1, 1000):
    cnt += check(i)
    if cnt == n:
        print(i)
        break