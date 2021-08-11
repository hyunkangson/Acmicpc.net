import sys

def kmp_table():
    j = 0
    table = [0] * len(word)
    for i in range(1, len(word)):
        while j > 0 and word[i] != word[j]:
            j = table[j-1]
        if word[i] == word[j]:
            j += 1
            table[i] = j

    return table


def kmp():
    j = 0
    global cnt
    table = kmp_table()
    for i in range(len(txt)):
        while j > 0 and txt[i] != word[j]:
            j = table[j-1]
        if txt[i] == word[j]:
            if j == len(word) - 1:
                cnt += 1
                val.append(i - len(word) + 2)
                j = table[j]
            else:
                j += 1


txt = sys.stdin.readline().replace("\n", "")
word = sys.stdin.readline().replace("\n", "")
val = []
cnt = 0
kmp()
print(cnt)
print(*val, end=" ")

