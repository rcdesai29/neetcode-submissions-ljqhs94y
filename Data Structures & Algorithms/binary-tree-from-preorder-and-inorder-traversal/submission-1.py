# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {value : index for index, value in enumerate(inorder)}
        self.p = 0

        def dfs(l, r):
            if l > r:
                return None
            
            r_v = preorder[self.p]
            self.p += 1
            root = TreeNode(r_v)
            mid = idx[r_v]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(inorder)-1)
