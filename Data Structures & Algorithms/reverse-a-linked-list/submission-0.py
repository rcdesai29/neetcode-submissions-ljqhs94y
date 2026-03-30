# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = head
        prev = None
      
        while c:
           t = c.next
           c.next = prev
           prev = c
           c = t

        return prev