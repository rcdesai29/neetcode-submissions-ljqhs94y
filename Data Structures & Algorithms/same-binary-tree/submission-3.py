# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(cur1, cur2):
            q = deque()
            if cur1 and cur2:
                q.append((cur1, cur2))
            elif not cur1 and not cur2:
                return True
            else:
                return False
            
            while q:
                for i in range(len(q)):
                    cur1, cur2 = q.popleft()
                    if cur1.val != cur2.val:
                        return False
                    if cur1.left and cur2.left:
                        q.append((cur1.left, cur2.left))
                    if (cur1.left and not cur2.left) or (cur2.left and not cur1.left):
                        return False
                    if cur1.right and cur2.right:
                        q.append((cur1.right, cur2.right))
                    if (cur1.right and not cur2.right) or( cur2.right and not cur1.right):
                        return False
            return True    

        return bfs(p, q)


            
            
        