class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def dfs(i, subset):
            if i >= len(s):
                res.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                cand = s[i:j+1]
                if (self.pali(cand)):
                    subset.append(cand)
                    dfs(j+1, subset)
                    subset.pop()
        dfs(0, [])
        return res

    def pali(self, string):
        l = 0
        r = len(string)-1
        while l < r:
            if string[l] != string[r]:
                return False
            l+= 1
            r -=1
        return True
        
        


