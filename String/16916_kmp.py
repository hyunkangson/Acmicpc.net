import sys

def make_table():
    j = 0
    table = [0] * len(word)
    for i in range(1,len(word)):
        while j and word[i] != word[j]:
            j = table[j-1]
        if word[i] == word[j]:
            j += 1
            table[i] = j
    return table


def kmp():
    table = make_table()
    j = 0
    for i in range(len(txt)):
        while j and txt[i] != word[j]:
            j = table[j-1]
        if txt[i] == word[j]:
            if j == len(word) - 1:
                print(1)
                exit()
            else:
                j += 1
    print(0)


txt = sys.stdin.readline().replace("\n","")
word = sys.stdin.readline().replace("\n","")
kmp()