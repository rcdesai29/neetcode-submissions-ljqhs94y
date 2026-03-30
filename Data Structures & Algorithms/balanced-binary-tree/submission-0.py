# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(cur):
            if not cur:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            if left > right:
                if left - right > 1:
                    return False
            elif right > left:
                if right - left > 1:
                    return False
            if left is False or right is False:
                return False
            else:
                return 1 + max(left, right)
        value = dfs(root)
        return value is not False