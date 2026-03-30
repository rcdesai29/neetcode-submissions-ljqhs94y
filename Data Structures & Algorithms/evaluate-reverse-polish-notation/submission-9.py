class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in ['+', '-', '*', '/']:
                stack.append(int(c))
            else:
                print(stack)
                second = (stack.pop())
                first = (stack.pop())
                if c == '+':
                    num = first + second
                elif c == '-':
                    num = first - second
                elif c == '*':
                    num = first * second
                elif c == '/':
                    num = int(first / second)
                stack.append(num)
        return stack[-1]
                