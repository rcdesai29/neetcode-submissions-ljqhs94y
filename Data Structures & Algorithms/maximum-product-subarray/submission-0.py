class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur = 1

        for n in nums:
            cur *= n
            res = max(res, cur)
            if cur == 0:
                cur = 1
        
        cur = 1
        for n in reversed(nums):
            cur *= n
            res = max(res, cur)
            if cur == 0:
                cur = 1
        return res