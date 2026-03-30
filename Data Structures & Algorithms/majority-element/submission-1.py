class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority element appears more then n/2
        # there is an majority element

        can = None
        count = 0

        for n in nums:
            if count == 0:
                can = n
            count += 1 if n == can else -1
        return can