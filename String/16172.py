import sys

def make():
    j = 0
    table = [0] * len(pattern)
    for i in range(1, len(pattern)):
        while j and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table


def kmp():
    j = 0
    for i in range(len(string)):
        while j and string[i] != pattern[j]:
            j = table[j-1]
        if string[i] == pattern[j]:
            if j == len(pattern)-1:
                print(1)
                exit()
            else:
                j += 1

    print(0)


string = sys.stdin.readline()
string = "".join([i for i in string if not i.isdigit()])
pattern = sys.stdin.readline()
table = make()
kmp()