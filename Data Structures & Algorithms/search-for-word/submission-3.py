class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r,c, i, visit):
            if i == len(word):
                return True

            if not (0<=r<len(board) and
                    0<=c<len(board[0]) and
                    (r,c) not in visit and
                    board[r][c] == word[i]):
                return False
            
            visit.add((r,c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i+1, visit):
                    return True
            visit.remove((r,c))
            return False

                    
                

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c, 0, set()):
                    return True
        return False