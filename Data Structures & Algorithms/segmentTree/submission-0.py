class Node:
    def __init__(self, total, L, R):
        self.total = total
        self.L = L
        self.R = R
        self.left = None
        self.right = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.builder(nums, 0, len(nums)-1)

    def builder(self,nums, L, R):
        if L == R:
            node = Node(nums[L], L, L)
            return node

        root = Node(0, L, R)

        M = (L + R) // 2

        root.left = self.builder(nums, L, M)
        root.right = self.builder(nums, M+1, R)

        root.total = root.left.total + root.right.total

        return root

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val, self.root.L, self.root.R)
    
    def update_helper(self, root, index, val, L, R):
        if L == R:
            root.total = val
            return 
        
        M = (L + R) // 2

        if M >= index:
            self.update_helper(root.left, index, val, L, M)
        else:
            self.update_helper(root.right, index, val, M+1, R)
        
        root.total = root.right.total + root.left.total
        return 
    
    def query(self, L: int, R: int) -> int:
        return self.query_helper(L,R, self.root)
    
    def query_helper(self,L, R, root):
        # not insde
        if root.L > R or root.R < L:
            return 0
        # completely inside
        elif root.L >= L and root.R <= R:
           return root.total
        else:
            return self.query_helper(L,R, root.left) +  self.query_helper(L,R, root.right)
           




