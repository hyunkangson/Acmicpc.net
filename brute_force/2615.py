import sys


def search(pos,n):
    dir = [(0,1),(1,1),(1,0),(1,-1)]
    for x,y in dir:
        cnt = 1
        d1 = 1
        d2 = 1
        for i in range(1,19):
            r = pos[0] + x * i
            c = pos[1] + y * i
            r2 = pos[0] - x * i
            c2 = pos[1] - y * i
            if 0 <= r < 19 and 0 <= c < 19:
                if board[r][c] == n and d1:
                    cnt += 1
                else:
                    d1 = 0
            if 0 <= r2 < 19 and 0 <= c2 < 19:
                if board[r2][c2] == n and d2:
                    cnt += 1
                else:
                    d2 = 0
        if cnt == 5:
            return True

    return False


board = [[0]*19 for _ in range(19)]
one = []
two = []

for i in range(19):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(19):
        if tmp[j]:
            board[i][j] = tmp[j]
            if tmp[j] == 2:
                two.append([i,j])
            else:
                one.append([i,j])


one2 = []
two2 = []

for o in one:
    x = search(o,1)
    if x:
        one2.append([o[0]+1,o[1]+1])

if two:
    for t in two:
        x = search(t,2)
        if x:
            two2.append([t[0]+1,t[1]+1])


if not one2 and not two2:
    print(0)
elif one2:
    one2.sort(key=lambda x:(x[1],x[0]))
    print(1)
    print(*one2[0])
elif two2:
    two2.sort(key=lambda x:(x[1],x[0]))
    print(2)
    print(*two2[0])