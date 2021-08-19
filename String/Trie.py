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


    def search(self, string):
        cur = self.root
        for char in string:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False

        if cur.flag:
            return True
        else:
            return False


    def start(self,prefix):
        cur = self.root
        bucket = []

        for p in prefix:
            if p in cur.children:
                cur = cur.children[p]
            else:
                return None

        cur = [cur]
        next_node = []
        while True:
            for node in cur:
                if node.flag:
                    bucket.append(node.flag)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                cur = next_node
                next_node = []
            else:
                break

        return bucket

trie = Trie()

