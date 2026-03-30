class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # m = s
        # n = p
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            
            if i >= len(s) and j >= len(p):
                return True

            if i < len(s) and j >= len(p):
                return False

            if i >= len(s):
                if j+1 < len(p) and p[j+1] == "*":
                    return dfs(i, j+2)
                else:
                    return False

            if j+1 < len(p) and p[j+1] == "*":
                matches = dfs(i, j+2) or (
                dfs(i+1, j) if s[i] == p[j] or p[j] == '.' else False)
            elif s[i] == p[j] or p[j] == ".":
                matches = dfs(i+1, j+1)
            else:
                return False
            
            memo[(i,j)] = matches
            return matches
        
        return dfs(0,0) 
         