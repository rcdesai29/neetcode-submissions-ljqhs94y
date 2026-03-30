class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        maxL = 0
        for i in hashset:
            length = 1
            while i + 1 in hashset:
                length += 1
                i+=1
            maxL = max(length, maxL)
        return maxL