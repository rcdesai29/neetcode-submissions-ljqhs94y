class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def generate(openN, closeN, n):
            if openN == closeN == n:
                return res.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                generate(openN+1, closeN, n )
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                generate(openN, closeN+1, n )
                stack.pop()
        generate(0,0,n)
        return res