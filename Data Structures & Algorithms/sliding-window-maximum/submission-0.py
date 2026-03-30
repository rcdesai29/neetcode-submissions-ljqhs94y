class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k-1
        array = []
        while r < len(nums):
            z = l
            res = nums[z]
            while z <= r:
                if nums[z] >= res:
                    res = nums[z]
                z+=1
            array.append(res)
            l+=1
            r+=1
        return array