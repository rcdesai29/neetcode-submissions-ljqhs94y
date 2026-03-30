class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = 1
        res = [1] * len(nums)

        for i, n in enumerate(nums):
            res[i] = pre
            pre *= n
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res

