import sys

class Node:
    def __init__(self, key, data=None):
        self.children = {}
        self.key = key
        self.flag = data


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        cur = self.root
        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.flag = string

    def start(self,n,cur):
        if n == 0:
            cur = self.root

        for c in sorted(cur.children.keys()):
            print("--"*n, c, sep="")
            self.start(n+1, cur.children[c])

n = int(sys.stdin.readline())
trie = Trie()

for _ in range(n):
    tmp = list(sys.stdin.readline().split())
    trie.insert(tmp[1:])

trie.start(0,None)