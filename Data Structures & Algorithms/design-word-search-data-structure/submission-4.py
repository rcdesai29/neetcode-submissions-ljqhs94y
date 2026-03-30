class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index, cur):

            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                if c not in cur.children:
                    return False
                
                cur = cur.children[c]

            return cur.isEnd
        
        return dfs(0, self.root)



