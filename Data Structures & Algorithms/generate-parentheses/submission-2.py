class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, temp):

            if open == close == n:
                res.append("".join(temp))
                return
            
            if open < n:
                temp.append('(')
                dfs(open + 1, close, temp)
                temp.pop()
            if close < open:
                temp.append(')')
                dfs(open, close + 1, temp)
                temp.pop()
            



        dfs(0, 0, [])
        return res