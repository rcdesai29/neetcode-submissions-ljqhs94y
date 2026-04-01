class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        q = deque([(sr, sc)])
        
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        visited = set()
        visited.add((sr,sc))
        og = image[sr][sc]
        while q:
            r, c = q.popleft()
            image[r][c] = color
            

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < len(image) and
                    0 <= nc < len(image[0]) and
                    (nr, nc) not in visited and
                    image[nr][nc] == og
                ):
                    q.append((nr, nc))
                    visited.add((nr,nc))
        return image
            