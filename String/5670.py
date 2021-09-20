import sys
from collections import defaultdict

try:
    while True:
        n = int(sys.stdin.readline())
        dic = defaultdict(list)
        words = []
        for i in range(n):
            word = sys.stdin.readline().rstrip()
            words.append(word)
            tmp = ""
            for w in word:
                if tmp != "" and w not in dic[tmp]:
                    dic[tmp].append(w)
                tmp += w

        ans = []
        for word in words:
            cnt = 1
            tmp = ""
            for w in word:
                if len(word) == 1:
                    break
                tmp += w
                if len(dic[tmp]) > 1 or tmp != word and tmp in words:
                    cnt += 1
            ans.append(cnt)

        print("{:.2f}".format(sum(ans)/n))

except:
    exit()