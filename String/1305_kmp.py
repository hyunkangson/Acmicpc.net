import sys

def make_table():
    j = 0
    table = [0] * len(txt)
    for i in range(1,len(txt)):
        while j and txt[i] != txt[j]:
            j = table[j-1]
        if txt[i] == txt[j]:
            j += 1
            table[i] = j

    print(len(table) - table[-1])

l = int(sys.stdin.readline())
txt = sys.stdin.readline().rstrip()
make_table()