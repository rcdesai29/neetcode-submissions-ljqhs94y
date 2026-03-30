class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p)+1): # we're adding 1 because we orginally removed one at the start
                p_Copy = p.copy()
                p_Copy.insert(i, nums[0])
                res.append(p_Copy)
        return res