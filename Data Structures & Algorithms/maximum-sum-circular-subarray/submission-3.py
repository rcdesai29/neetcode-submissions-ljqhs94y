class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum) 
        
        # Finding min subArray
        minSum = nums[0]
        curSum = 0
        for n in nums:
            if curSum > 0:
                curSum = 0
            curSum += n
            minSum = min(minSum, curSum) 
        if maxSum < 0:
            return maxSum
        maxSum = max(maxSum, sum(nums) - minSum)
        return maxSum
        
        