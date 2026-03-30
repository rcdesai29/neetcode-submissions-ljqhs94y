class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = None
    
    def addWord(self, word):
        root = self

        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.isWord = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        res = []
        rows, cols = len(board), len(board[0])

        def dfs(r,c,node):
            if (r<0 or c<0 or
                r>=rows or c>=cols or
                board[r][c] == '#' or  
                board[r][c] not in node.children):
                return
            
            char = board[r][c]
            node = node.children[char]
            if node.isWord:
                res.append(node.isWord)
                node.isWord = None
            
            board[r][c] = "#"

            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c+1,node)
            dfs(r,c-1,node)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root)
        return res
