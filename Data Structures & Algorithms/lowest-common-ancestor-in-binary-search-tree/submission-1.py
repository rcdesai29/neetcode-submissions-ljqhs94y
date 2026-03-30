# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if cur.val > p.val and cur.val > q.val: # its lower so Left Side
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val: # its greater so Right Side
                cur = cur.right
            else:
                return cur
        return None