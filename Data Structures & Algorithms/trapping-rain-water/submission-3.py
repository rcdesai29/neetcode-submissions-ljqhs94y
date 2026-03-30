class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        """
        walls? wall behind it
        """
        maxLeftWall = height[0]
        maxRightWall = height[len(height)-1]
        res = 0
        while l<r:
            if height[l] < height[r]:
                l += 1
                maxLeftWall = max(maxLeftWall, height[l])
                res += maxLeftWall - height[l]
            else:
                r -=1
                maxRightWall = max(maxRightWall, height[r])
                res += maxRightWall - height[r]
        return res



