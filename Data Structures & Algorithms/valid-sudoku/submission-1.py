class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)  
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                value = board[i][j]
                if value != '.':
                    if (
                        value in row[i] or
                        value in col[j] or
                        value in square[i//3, j//3]):
                        return False
                    row[i].add(value)
                    col[j].add(value)
                    square[(i//3, j//3)].add(value)
        return True
                    
