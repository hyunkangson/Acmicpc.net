import sys

words = []
for _ in range(int(sys.stdin.readline())):
    txt = sys.stdin.readline().rstrip()
    tmp = ""
    tmp2 = []
    for i in txt:
        if i.isdigit():
           tmp += i
        else:
            if tmp:
                tmp2.append(str(int(tmp)))
            tmp2.append(i)
            tmp = ""

    if tmp:
        tmp2.append(str(int(tmp)))

    words.append(["".join(tmp2),txt])
print(words)
print(sorted(words))