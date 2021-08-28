import sys
from collections import defaultdict

def check():
    cnt = 0
    tmp = [0,0]

    for i in range(5):
        tmp2 = [0,0]
        for j in range(5):
            tmp2[0] += bingo[i][j]
            tmp2[1] += bingo[j][i]
        if tmp2[0] == 5:
            cnt += 1
        if tmp2[1] == 5:
            cnt += 1

        tmp[0] += bingo[i][i]
        tmp[1] += bingo[i][4 - i]


    if tmp[0] == 5:
        cnt += 1
    if tmp[1] == 5:
        cnt += 1

    if cnt >= 3:
        return 1
    else:
        return 0


dic = defaultdict(int)
bingo = [[0]*5 for _ in range(5)]

r = c = 0
for _ in range(5):
    nums = list(map(int, sys.stdin.readline().split()))
    for n in nums:
        dic[n] = [r,c]
        c += 1
        if c == 5:
            c = 0
            r += 1

cnt = 0
for _ in range(5):
    nums = list(map(int, sys.stdin.readline().split()))
    for n in nums:
        cnt += 1
        r, c = dic[n]
        bingo[r][c] = 1
        if check():
            print(cnt)
            exit()
