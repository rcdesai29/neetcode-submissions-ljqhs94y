class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subs = []
        i = 0
        res = []
        nums.sort()
        def dfs(i):
            if i>=len(nums):
                res.append(subs[:])
                return
            subs.append(nums[i])
            dfs(i+1)
            subs.pop()
            while i<len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(i)
        return res
