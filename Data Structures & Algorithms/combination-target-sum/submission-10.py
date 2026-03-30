class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(total, i, temp):
            if total == target:
                res.append(temp[:])
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    continue
                temp.append(nums[j])
                dfs(total + nums[j], j, temp)
                temp.pop()
            
            
        dfs(0, 0, [])
        return res