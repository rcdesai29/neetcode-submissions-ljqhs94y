class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 != 0:
            return False
        
        target = sum(nums) / 2


        dp = {}
        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i,total)]
            
            if total == target:
                dp[(i, total)] = True
                return True
            
            if i >= len(nums) or total > target:
                dp[(i, total)] = False
                return False
            
            if dfs(i+1, total + nums[i]):
                dp[(i, total)] = True
                return True
            if dfs(i+1, total):
                dp[(i, total)] = True
                return True
            dp[(i, total)] = False
            return False
        return dfs(0, 0)
                
