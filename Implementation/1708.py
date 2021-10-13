import sys


def dist(p1,p2):
    return (p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1])


def ccw(p1,p2,p3):
    cross_product = (p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])
    if cross_product > 0:
        return 1
    elif cross_product < 0:
        return -1
    else:
        return 0


def comp(left,right):
    ret = 0
    direction = ccw(p,left,right)
    if direction == 0:
        ret = (dist(p, left) < dist(p,right))
    elif direction == 1:
        ret = 1
    else:
        ret = 0
    return ret


def quick(low, high):
    if high - low <= 0:
        return

    pivot = coord[low + (high - low + 1) // 2]
    i,j = low, high

    while i <= j:
        while comp(coord[i],pivot):
            i += 1
        while comp(pivot,coord[j]):
            j -= 1
        if i > j:
            break
        tmp = coord[i]
        coord[i] = coord[j]
        coord[j] = tmp
        i += 1
        j -= 1

    quick(low,j)
    quick(i, high)


n = int(sys.stdin.readline())
coord = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x:(x[1],x[0]))
p = coord[0]

quick(1,n-1)

def leftside(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])


i = 2
stack = [coord[0],coord[1]]

while i < n:
    x = leftside(stack[-2],stack[-1],coord[i])
    if x > 0:
        stack.append(coord[i])
    elif x == 0:
        stack[-1] = coord[i]
    else:
        stack.pop()
        continue
    i += 1

print(len(stack))