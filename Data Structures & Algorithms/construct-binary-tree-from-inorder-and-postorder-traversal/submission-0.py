# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #inorder [left, root, right]
        #postorder [left, right, root]

        def dfs(inorder, postorder):
            if not inorder or not postorder:
                return 
            
            # root
            root = TreeNode(postorder[-1])

            idx = inorder.index(postorder[-1])
            # left half
            root.left = dfs(inorder[:idx], postorder[:idx])
            # right half
            root.right = dfs(inorder[idx+1:], postorder[idx:-1])

            return root
        return dfs(inorder, postorder)