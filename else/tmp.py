a = input().split('-')
num = []
for i in a:
    ## 작성 부분 ##
    for j in i.split("+"):
        num.append(int(j))
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)