class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        path1 = []
        path2 = []
        dp = {}
        def dfs(i, path1, path2):
            key = (tuple(path1), tuple(path2))
            if key in dp:
                return dp[key]
            
            if i == len(nums):
                return sum(path1) == sum(path2)

            path1.append(nums[i])
            if dfs(i+1, path1, path2):
                dp[key] = True
                return True
            else:
                path1.pop()
            
            path2.append(nums[i])
            if dfs(i+1, path1, path2):
                dp[key] = True
                return True
            else:
                path2.pop()
            dp[key] = False
            return False
        return dfs(0, [], [])