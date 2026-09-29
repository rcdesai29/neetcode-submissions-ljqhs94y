class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        
        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))
        length = 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r == rows-1 and c == cols-1:
                    return length
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] != 1 and
                        (nr,nc) not in visit
                    ):
                        continue
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        return -1
