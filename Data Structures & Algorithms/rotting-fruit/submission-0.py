class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0
        seconds = 0
        q = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while fresh != 0 and q:
            length = len(q)
            
            for i in range(length):
                r,c = q.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if not (
                        0<= row < len(grid) and
                        0<= col < len(grid[0]) and
                        grid[row][col] == 1
                        ):
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))
            seconds += 1
        return seconds if fresh == 0 else -1

