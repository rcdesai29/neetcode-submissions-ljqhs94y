class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        path = path.split('/')

        for cur in path:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
            
        return "/" + "/".join(stack)