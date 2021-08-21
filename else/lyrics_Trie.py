class Node():
    def __init__(self,key,data=None):
        self.key = key
        self.flag = data
        self.children = {}

class Trie():
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        cur = self.root
        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.flag = string

    def start(self, prefix):
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



def solution(words, queries):
    trie_pfx = Trie()
    trie_sfx = Trie()
    for w in words:
        trie_sfx.insert(w[::-1])
        trie_pfx.insert(w)

    ans = []
    for q in queries:
        l = len(q)
        tmp = []
        if q[0] == "?":
            tmp = trie_sfx.start(q.replace("?","")[::-1])
        else:
            tmp = trie_pfx.start(q.replace("?",""))

        if tmp:
            cnt = 0
            for t in tmp:
                if len(t) == l:
                    cnt += 1
            ans.append(cnt)
        else:
            ans.append(0)

    return ans

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"])