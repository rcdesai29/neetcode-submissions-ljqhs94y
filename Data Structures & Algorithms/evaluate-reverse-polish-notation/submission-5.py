class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {
            "+" : "+",
            "*" : "*",
            "-" : "-",
            "/" : "/",

        }

        for c in tokens:
            if c in op:
                val2 = (stack.pop())
                val1 = (stack.pop())
                if op[c] == "+":
                    res = val1 + val2
                    stack.append(res)
                elif op[c] == "*":
                    res = val1 * val2
                    stack.append(res)
                elif op[c] == "-":
                    res = val1 - val2
                    stack.append(res)
                elif op[c] == "/":
                    res = int(val1 / val2)
                    stack.append(res)
            else:
                stack.append(int(c))
        return stack[-1]