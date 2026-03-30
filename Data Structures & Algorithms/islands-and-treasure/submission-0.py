class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #chaning them in place

        directions = [(-1, 0), (1,0), (0,1), (0,-1)]
        inf = 2 ** 31 -1

        q = deque([])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c, 0))
        
        while q:
            qLen = len(q)

            for i in range(qLen):
                r,c, distance = q.popleft()

                # move thru the 0s
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == inf):
                        continue
                    grid[nr][nc] = distance + 1
                    q.append((nr, nc, distance + 1))
        
                    
                    
                    
