class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visit = set()
        row = len(grid)
        col = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i, j):
            if not (
                0 <= i < row and 0 <= j < col and
                grid[i][j] == 1 and (i,j) not in visit
            ):
                return 0
            
            visit.add((i,j))
            area = 1
            for dr, dc in directions:
                area += dfs(i + dr, j + dc)
            return area

        res = 0
        for i in range(row):
            for j in range(col):
                res = max(res, dfs(i, j))
        return res
        