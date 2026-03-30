class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        i = 0

        def dfs(i, sub, total):
            if total == target:
                res.append(sub[:])
                return
            if total > target or i>= len(nums):
                return
            
            sub.append(nums[i])
            dfs(i, sub, total + nums[i])
            sub.pop()
            dfs(i+1, sub, total)
        dfs(i, [], 0)
        return res
            
