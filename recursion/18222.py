import sys
n = int(sys.stdin.readline())

def recurs(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x % 2== 0:
        return recurs(x//2)
    else:
        return 1 - recurs(x//2)

print(recurs(n-1))