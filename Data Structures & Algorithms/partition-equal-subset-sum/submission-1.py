class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False


        subset1 = []
        subset2 = []
        dp = {}
        def dfs(subset1, subset2, i):
            key = (tuple(subset1), tuple(subset2))
            if key in dp:
                return dp[key]
            
            
            if i == len(nums):
                return sum(subset1) == sum(subset2)
            
            
            subset1.append(nums[i])
            if dfs(subset1, subset2, i+1):
                dp[key] = True
                return True
            else:
                subset1.pop()
            subset2.append(nums[i])
            if dfs(subset1, subset2, i+1):
                dp[key] = True
                return True
            else:
                subset2.pop()

            dp[key] = False
            return False
        
        return dfs([], [], 0)