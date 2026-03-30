class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False
    
    def addWord(self, word):
        node = self
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        res, visit = set(), set()

        def dfs(r, c, node, word):
            #base case
            if not (0<= r < len(board) and 
                    0<= c < len(board[0]) and
                    (r,c) not in visit and
                    board[r][c] in node.child):
                    return
                
            visit.add((r,c))
            char = board[r][c]
            node = node.child[char]
            word += char

            if node.isWord:
                res.add(word)
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)

            visit.remove((r,c))


        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, "")
        return list(res)