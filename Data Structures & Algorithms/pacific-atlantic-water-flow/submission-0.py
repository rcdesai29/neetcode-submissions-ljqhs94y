class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = False, False
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r,c, prev):
            nonlocal pac
            nonlocal atl

            #Hits PAC
            if (r<0 or c<0):
                pac = True
                return
            
            #Hits ATL
            if (r>=rows or c>=cols):
                atl = True
            
            
            if ( 0<=r<rows and 0<=c<cols):
                if (heights[r][c] > prev):
                    return
            
                tmp = heights[r][c]
                heights[r][c] = float('inf')
                for dr, dc in directions:
                    dfs(r + dr, c+dc, tmp)
                    if atl and pac:
                        break

                heights[r][c] = tmp

        # Go thru entire graph:
        res = []
        for r in range(rows):
            for c in range(cols):
                pac, atl = False, False
                dfs(r,c, float('inf'))
                if pac and atl:
                    res.append([r,c])
        return res