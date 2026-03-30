class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, path):
            res.append(path.copy())
            if i == len(nums):
                return
            
            prev = None
            for j in range(i, len(nums)):
                if nums[j] == prev:
                    continue
                path.append(nums[j])
                dfs(j + 1, path)
                path.pop()
                prev = nums[j]

        dfs(0, [])
        return res