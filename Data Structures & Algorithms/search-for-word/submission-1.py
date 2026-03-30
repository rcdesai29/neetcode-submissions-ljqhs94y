class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [
            (1,0), (-1,0), (0,1), (0,-1)
        ]

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if not (0<=r<len(board) and 0<=c<len(board[0]) and
                    word[i] == board[r][c]):
                return False
            char = board[r][c]
            board[r][c] = '#'
            for dr, dc in directions:
                newR = r + dr
                newC = c + dc
                res = dfs(newR, newC, i + 1)
                if res:
                    board[r][c] = char
                    return True
            board[r][c] = char
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False
