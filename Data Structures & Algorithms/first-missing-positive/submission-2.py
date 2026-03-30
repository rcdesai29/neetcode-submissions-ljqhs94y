class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)

        n = len(nums)+1
        res = 1
        for i in range(1, n+1):
            if i in nums:
                res += 1
            else:
                return i
        return res