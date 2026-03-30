class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        i = 0

        candidates.sort()
        def dfs(i, sub, total):
            if total == target:
                res.append(sub[:])
                return
            if total >= target or i>= len(candidates):
                return
            
            sub.append(candidates[i])
            dfs(i+1, sub, total + candidates[i])
            sub.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, sub, total)


        dfs(i, [], 0)
        return res