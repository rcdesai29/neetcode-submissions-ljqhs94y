class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1

        maxVol = 0
        
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            if area > maxVol:
                maxVol =max(area, maxVol)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxVol
