class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        root = self

        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r>= ROWS or c>=COLS or #bottom and right
                r<0 or c<0 or #top and left
                (r,c) in visit or board[r][c] not in node.children):
                return
            
            char = board[r][c]
            word += char
            node = node.children[char]

            if node.isWord:
                res.add(word)
            
            
            visit.add((r,c))

            dfs(r+1, c, node, word) #bottom
            dfs(r-1, c, node, word) #top
            dfs(r, c+1, node, word) #right
            dfs(r, c-1, node, word) #left

            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")
        return list(res)

