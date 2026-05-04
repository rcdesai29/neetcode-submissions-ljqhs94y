class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def backtrack(i, cur_sum):
            if i == len(nums):
                return cur_sum == target
            
            return (
                backtrack(i+1, cur_sum + nums[i]) +
                backtrack(i+1, cur_sum - nums[i])
            )
    
        return backtrack(0,0)