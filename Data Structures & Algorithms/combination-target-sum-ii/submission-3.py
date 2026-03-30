class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(idx, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                if (total + candidates[i]) > target:
                    continue
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()
                prev = candidates[i]
                
        dfs(0, [], 0)
        return res




        