class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dont' start at egdes
        directions = {(1,0), (-1,0), (0,-1), (0,1)}
        
        def dfs(r,c):
            if not (
                0 <= r < len(board) and
                0 <= c < len(board[0]) and
                board[r][c] == 'O'
            ):
                return 
            
            board[r][c] = "T"
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    if r in [0, len(board)-1] or c in [0, len(board[0])-1]:
                        dfs(r,c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'T':
                    board[r][c] = 'O'