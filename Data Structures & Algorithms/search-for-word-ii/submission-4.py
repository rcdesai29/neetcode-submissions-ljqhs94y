class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self # root node is just self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(board)
        cols = len(board[0])
        res = []
        visited = set()

        def dfs(r,c, node, path):
            if not (
                0 <= r < rows and
                0 <= c < cols and
                board[r][c] in node.children and
                (r,c) not in visited
            ):
                return
            
            visited.add((r,c))
            path += board[r][c]
            cur = node.children[board[r][c]]

            if cur.isWord:
                res.append(path)
                cur.isWord = False
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, cur, path)
            
            visited.remove((r,c))
            if not cur.children:
                del node.children[board[r][c]]
            return


        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root, "")
        
        return res