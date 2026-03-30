class Trie:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root

        stack = [(0, cur)]

        while stack:
            index, cur = stack.pop()

            if index == len(word):
                if cur.eow:
                    return True
                continue
            
            char = word[index]

            if char == ".":
                for child in cur.children.values():
                    stack.append((index+1, child))
            else:
                if char in cur.children:
                    stack.append((index+1, cur.children[char]))
        return False
