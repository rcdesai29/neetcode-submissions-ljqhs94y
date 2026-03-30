class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def dfs(i, subset):
            if i >= len(s):
                res.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                cand = s[i:j+1]
                if cand == cand[::-1]:
                    subset.append(cand)
                    dfs(j+1, subset)
                    subset.pop()
        dfs(0, [])
        return res
        
        


