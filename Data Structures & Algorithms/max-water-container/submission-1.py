class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxL = heights[l]
        maxR = heights[r]
        res = 0
        while l<r:
            water = min(maxL, maxR) * (r-l)
            if maxL < maxR:
                l+=1
                maxL = max(maxL, heights[l])
            else:
                r-=1
                maxR = max(maxR, heights[r])
            res = max(res, water)
        return res
