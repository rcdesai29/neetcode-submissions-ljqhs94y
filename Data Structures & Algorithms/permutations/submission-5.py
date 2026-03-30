class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = set()

        def bt(path):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                bt(path)
                path.pop()
                used.remove(nums[i])
        
        bt([])
        return res