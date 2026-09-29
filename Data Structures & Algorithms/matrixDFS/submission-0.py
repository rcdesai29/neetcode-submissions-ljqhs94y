class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r,c):
            if not (
                0 <= r < rows and 
                0 <= c < cols and
                grid[r][c] == 0 and
                (r,c) not in visited
            ):
                return 0
            if r == rows-1 and c == cols-1:
                return 1
            count = 0
            visited.add((r,c))
            for dr, dc in directions:
                count +=  dfs(r + dr, c + dc)
            visited.remove((r,c))      
            return count
        return dfs(0,0)
        