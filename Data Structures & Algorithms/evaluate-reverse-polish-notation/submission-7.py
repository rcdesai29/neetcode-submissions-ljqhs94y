class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                val2 = (stack.pop())
                val1 = (stack.pop())
                res = val1 + val2
                stack.append(res)
            elif c == "*":
                val2 = (stack.pop())
                val1 = (stack.pop())
                res = val1 * val2
                stack.append(res)
            elif c == "-":
                val2 = (stack.pop())
                val1 = (stack.pop())
                res = val1 - val2
                stack.append(res)
            elif c == "/":
                val2 = (stack.pop())
                val1 = (stack.pop())
                res = int(val1 / val2)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[-1]