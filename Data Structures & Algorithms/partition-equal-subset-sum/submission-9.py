class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) / 2
        dp = {}

        def dfs(i, curSum):
            if (i, curSum) in dp:
                return dp[(i, curSum)]

            if curSum == target:
                dp[(i, curSum)] = True
                return True
            if i >= len(nums) or curSum > target:
                dp[(i, curSum)] = False
                return False

            if dfs(i + 1, curSum + nums[i]):
                dp[(i, curSum)] = True
                return True
            if dfs(i + 1, curSum):
                dp[(i, curSum)] = True
                return True
            dp[(i, curSum)] = False
            return False

        return dfs(0, 0)