import math
def solution(n):
    n = math.sqrt(n)
    if n == int(n):
        return (n+1)**2
    else:
        return -1
