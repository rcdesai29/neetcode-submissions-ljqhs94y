# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        cur = slow.next
        slow.next = None

        prev = None
        while cur:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        while head and prev:
            t = head.next
            z = prev.next
            head.next = prev
            prev.next = t
            head = t
            prev = z
            
            
            
            
        
        

        

