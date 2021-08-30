import sys

def hanoi(n,fr,pos,to):
    if n == 0:
        return
    hanoi(n-1, fr, to, pos)
    print(fr,to)
    hanoi(n-1,pos,fr,to)


n = int(sys.stdin.readline())
print(2**n-1)
if n <= 20:
    hanoi(n,1,2,3)