"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        og = head
        while og:
            copy = Node(og.val)
            copy.next = og.next
            og.next = copy
            og = copy.next
        
        newHead = head.next
        og = head
        while og:
            if og.random is not None:
                og.next.random = og.random.next
            og = og.next.next
        
        og = head
        while og:
            copy = og.next
            og.next = copy.next
            if copy.next is not None:
                copy.next = copy.next.next
            og = og.next
        return newHead
       
