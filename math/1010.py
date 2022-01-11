import sys,math

def factorial(n):
    tmp = 1
    for i in range(2,n+1):
        tmp *= i
    return tmp


t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())
    print(factorial(m)//(factorial(m-n)*factorial(n)))