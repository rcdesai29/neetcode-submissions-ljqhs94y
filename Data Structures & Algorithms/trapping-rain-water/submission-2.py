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
            if maxLeftWall > height[l]:
                leftTrapped = maxLeftWall - height[l]
                res += leftTrapped
            elif maxLeftWall <= height[l]:
                maxLeftWall = height[l]
            
            if maxRightWall > height[r]:
                rightTrapped = maxRightWall - height[r]
                res += rightTrapped
            elif maxRightWall <= height[r]:
                maxRightWall = height[r]

            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return res



