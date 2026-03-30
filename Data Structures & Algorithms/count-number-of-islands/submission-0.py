class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                r,c = q.popleft()
                visit.add((r,c))
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (0<=nr<rows and
                        0<=nc<cols and
                        (nr,nc) not in visit and
                        grid[nr][nc] == "1"):
                        q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands