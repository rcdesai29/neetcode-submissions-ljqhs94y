class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def bt(i, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            subset.append(nums[i])
            bt(i, total+nums[i])
            subset.pop()
            bt(i+1, total)
        bt(0, 0)
        return res