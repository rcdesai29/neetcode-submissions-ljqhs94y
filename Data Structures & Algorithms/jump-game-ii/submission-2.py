class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cur = 0
        farthest = 0
        jumps = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if cur == i:
                cur = farthest
                jumps += 1
        return jumps
        