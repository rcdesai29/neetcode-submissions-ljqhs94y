class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i>= len(s) and j >= len(p):
                return True
            
            if i >= len(s):
                if j + 1 < len(p) and p[j + 1] == '*':
                    memo[(i,j)] =  dfs(i, j+2)
                    return memo[(i,j)]
                else:
                    return False
            if j>= len(p):
                return False
            
            same = True if s[i] == p[j] or p[j] == '.' else False
            if j+1 < len(p) and p[j+1] == '*':
                if same:
                    memo[(i,j)] = dfs(i+1, j) or dfs(i, j+2)
                else:
                    memo[(i,j)] = dfs(i, j+2)
            else:
                if same:
                    memo[(i,j)] = dfs(i + 1 , j + 1 )
                else:
                    memo[(i,j)] = same
            return memo[(i,j)]
            
        return dfs(0,0)