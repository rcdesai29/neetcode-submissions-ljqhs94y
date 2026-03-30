class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, subset):
            res.append(subset.copy())

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j +1, subset)
                subset.pop()

        dfs(0, [])
        return res