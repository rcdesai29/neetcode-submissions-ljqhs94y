class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        q = deque([])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c, 0))
        

        while q:
            qLen = len(q)

            for i in range(qLen):
                r,c, distance = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 2**31 -1):
                        continue
                    
                    grid[nr][nc] = distance + 1
                    q.append((nr, nc, distance + 1))
        
