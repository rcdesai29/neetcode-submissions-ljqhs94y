class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        row = len(picture)
        col = len(picture[0])

        row_count = [0] * row
        col_count = [0] * col

        for r in range(row):
            for c in range(col):
                if picture[r][c] == 'B':
                    row_count[r] += 1
                    col_count[c] += 1
        res = 0
        for r in range(row):
            for c in range(col):
                if picture[r][c] == 'B':
                    if row_count[r] == 1 and col_count[c] == 1:
                        res += 1
        return res

        