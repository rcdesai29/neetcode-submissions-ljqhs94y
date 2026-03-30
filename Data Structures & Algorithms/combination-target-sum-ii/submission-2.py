class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(nums):
                return
            
            cur.append(nums[i])
            dfs(i+1, cur, total + nums[i])
            cur.pop()

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res