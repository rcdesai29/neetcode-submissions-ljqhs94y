class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subs = []
        i = 0
        res = [[]]
        def dfs(i):
            if i>=len(nums):
                return
            
            subs.append(nums[i])
            dfs(i+1)
            res.append(subs[:])
            subs.pop()
            dfs(i+1)
            
        dfs(i)
        return res