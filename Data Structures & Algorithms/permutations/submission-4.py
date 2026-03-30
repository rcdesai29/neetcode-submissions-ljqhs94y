class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def bt(path, used):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                bt(path, used)
                path.pop()
                used[i] = False
        
        bt([], [False] * n)
        return res