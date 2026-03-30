class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {len(nums)-1 : True}

        def dfs(i):
            if i in memo:
                return memo[i]

            
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i+1, end):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)