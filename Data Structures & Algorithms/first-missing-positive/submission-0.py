class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        largest = 0
        smallest = nums[0]
        for n in nums:
            largest = max(n, largest)
            smallest = min(n, smallest)
        
        
        res = [0] * largest
        for n in nums:
            if 0 < n < largest:
                res[n] += 1
        
        for i in range(1, len(res)):
            if res[i] == 0:
                return i
        return largest + 1


