class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        def dfs(i, cur):
            # got to figure out the base case
            if cur not in res:
                res.append(cur.copy())
            if i>= len(nums):
                return 

            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
            dfs(i+1, cur)
        
        dfs(0, [])
        return res