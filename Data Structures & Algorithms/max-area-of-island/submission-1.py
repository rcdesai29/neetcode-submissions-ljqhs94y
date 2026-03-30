class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):

            if not (
                0<=r<rows and 0<=c<cols and
                (r,c) not in visited and
                grid[r][c] != 0
            ):
                return 0
            
            area = 1
            visited.add((r,c))
            for dr, dc in directions:
                area += dfs(dr + r, dc + c)
            return area

        


        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i,j))
        return res