class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        
        trapped_water = 0
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if height[l] < height[r]:
                #max water from left side
                maxL = max(maxL, height[l])
                trapped_water += maxL - height[l]
                l+=1
            else:
                #max water from right side
                maxR = max(maxR, height[r])
                trapped_water += maxR - height[r]
                r-=1



        return trapped_water

                