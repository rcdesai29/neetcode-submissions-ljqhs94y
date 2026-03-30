class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        colum = defaultdict(set)
        subgrid = defaultdict(set)

        for i in range(9): #row
            for j in range(9): #column
                num = board[i][j]

                if num ==".":
                    continue
                key = (i//3, j//3)
                if ((num in row[i]) or (num in colum[j]) or (num in subgrid[key])):
                    return False
               
                subgrid[key].add(num)
                row[i].add(num)
                colum[j].add(num)
        return True
                
                
