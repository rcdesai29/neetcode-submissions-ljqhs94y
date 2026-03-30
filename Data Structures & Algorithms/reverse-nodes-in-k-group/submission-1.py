# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0

        while cur and count < k:
            count += 1
            cur = cur.next
        if count < k:
            return head
        
        prev, cur = None, head
        for i in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        head.next = self.reverseKGroup(cur, k)

        return prev