import sys

n = int(sys.stdin.readline())
m = 10 ** 6
p = 15 * (10 ** 5)
fibo = [0,1]

if n < 2:
    print(fibo[n])

for i in range(2,p):
    fibo.append((fibo[i-1]+fibo[i-2])%m)
    if i == n:
        print(fibo[n%p])
        exit()

print(fibo[n%p])