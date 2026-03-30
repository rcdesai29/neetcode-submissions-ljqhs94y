class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range (len(board[0])):
                char = board[r][c]
                if char != '.':
                    if (
                        char  in rows[r] or
                        char  in cols[c] or
                        char  in squares[r//3, c//3]
                    ):
                        return False
                
                    rows[r].add(char)
                    cols[c].add(char)
                    squares[r//3, c//3].add(char)
        return True
                    


