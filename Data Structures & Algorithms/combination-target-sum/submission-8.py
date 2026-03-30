class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(total, cur, i):
            if total == target:
                res.append(cur[:])
                return
            
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            dfs(total + nums[i], cur, i)
            cur.pop()
            dfs(total, cur, i+1)
        dfs(0, [], 0)
        return res
