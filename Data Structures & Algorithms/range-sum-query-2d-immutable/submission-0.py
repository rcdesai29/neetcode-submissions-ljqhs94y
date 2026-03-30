class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        [[1,2]
         [3,4]]
        
        [[0,0,0]
         [0,1,2]
         [0,3,4]]
         goal is to treat every position as if it was the bottom right sum
        """
        rows, cols = len(matrix), len(matrix[0])
        self.preMatrix = [[0] * (cols + 1) for r in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.preMatrix[r][c+1]
                self.preMatrix[r+1][c+1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1 = row1 + 1, col1 + 1
        row2, col2 = row2 + 1, col2 + 1

        bottomRight = self.preMatrix[row2][col2]
        above = self.preMatrix[row1 - 1][col2]
        left = self.preMatrix[row2][col1 - 1]
        topLeft = self.preMatrix[row1 -1][col1 - 1]
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)