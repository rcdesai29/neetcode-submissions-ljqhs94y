class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        m = len(ans)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n - m] = nums[i]
        return ans