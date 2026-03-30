class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(sub):
            if len(sub) == len(nums):
                res.append(sub[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    sub.append(nums[i])
                    dfs(sub)
                    sub.pop()
                    used.remove(nums[i])
            
        dfs([])
        return res