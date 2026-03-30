class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority element appears more then n/2
        # there is an majority element

        stack = []

        for n in nums:
            if stack and n != stack[-1]:
                stack.pop()
            
            if not stack or n == stack[-1]:
                stack.append(n)
        return stack[-1]