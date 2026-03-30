class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # turn border O to T

        rows = len(board)
        cols = len(board[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visit = set()

        def dfs(r, c):
            if not (
                0<= r < rows and 0<= c < cols and
                (r,c) not in visit and board[r][c] == 'O'
            ):
                return
            visit.add((r,c))
            board[r][c] = 'T'
            for dr, dc in directions:
                dfs(dr + r, dc + c)

        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][cols-1] == 'O':
                dfs(r, cols-1)
            
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows-1][c] == "O":
                dfs(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
       
        

