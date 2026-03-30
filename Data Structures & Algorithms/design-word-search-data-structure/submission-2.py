class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        stack = [(0, cur)]

        while stack:

            index, cur = stack.pop()

            if index == len(word):
                if cur.word:
                    return True
                continue 
            
            char = word[index]

            for c in char:
                if c == ".":
                    for child in cur.children.values():
                        stack.append((index+1, child))
                else:
                    if c in cur.children:
                        stack.append((index+1, cur.children[c]))
        return False
        
