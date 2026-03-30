class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = {}

        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i < len(s) and j>= len(p):
                return False

            if i >= len(s):
                if j >= len(p):
                    return True
                elif j + 1 < len(p) and p[j +1 ] == '*':
                    return dfs(i, j+2)
                else:
                    return False
            
            if j+1 < len(p) and p[j + 1] == '*':
               match = dfs(i, j + 2) or ( 
                dfs(i+1, j) if s[i] == p[j] or p[j] == '.' else False)
            elif s[i] == p[j] or p[j] == '.':
                match = dfs(i+1, j+1)
            else:
                return False
            
            dp[(i,j)] = match
            return match

        return dfs(0,0)