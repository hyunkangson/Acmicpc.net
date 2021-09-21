import sys

n = int(sys.stdin.readline())
words = []
for i in range(n):
    txt = sys.stdin.readline().rstrip()
    tmp = ""
    tmp2 = []
    for j in range(len(txt)):
        if txt[j].isdigit():
            tmp += txt[j]
        elif txt[j].isupper():
            if tmp:
                cnt = tmp.count("0")
                tmp2.append(0)
                tmp2.append(int(tmp) + cnt * 0.01)
                tmp = ""
            tmp2.append(1)
            tmp2.append(ord(txt[j]))
        else:
            if tmp:
                cnt = tmp.count("0")
                tmp2.append(0)
                tmp2.append(int(tmp) + cnt * 0.01)
                tmp = ""
            tmp2.append(1)
            tmp2.append(ord(txt[j])-31.5)

    if tmp:
        cnt = tmp.count("0")
        tmp2.append(0)
        tmp2.append(int(tmp) + cnt * 0.01)

    words.append([tmp2,txt])


words.sort()
for i in range(n):
    print(words[i][1])