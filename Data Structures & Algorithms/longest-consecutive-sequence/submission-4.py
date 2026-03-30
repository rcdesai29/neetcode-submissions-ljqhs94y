class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        consec = set(nums)
        res = 1
        for n in nums:
            temp = 1
            while n+1 in consec:
                temp += 1
                n += 1
            res = max(temp, res)
        return res

            