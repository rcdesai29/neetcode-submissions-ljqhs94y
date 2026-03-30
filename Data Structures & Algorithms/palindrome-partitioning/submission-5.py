class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                partial = s[i:j+1]
                if self.pali(partial):
                    part.append(partial)
                    dfs(j+1)
                    part.pop()
        

        dfs(0)
        return res
    

    def pali(self, string):
        return string == string[::-1]