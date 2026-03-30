class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        can = None
        count = 0
        for n in nums:
            if count == 0:
                can = n
            count += 1 if n == can else -1
        return can
