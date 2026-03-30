class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        i = 0
        res = []
        def dfs(i, subs):
            if sum(subs) == target:
                res.append(subs[:])
                return
            if sum(subs) > target or i>= len(nums):
                return
            
            
            subs.append(nums[i])
            dfs(i, subs)
            subs.pop()
            dfs(i+1, subs)
            

        dfs(i, [])
        return res