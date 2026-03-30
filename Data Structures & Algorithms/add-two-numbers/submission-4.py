# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            newVal = v1 + v2 + carry
            carry = newVal // 10

            val = ListNode(newVal % 10) 
            cur.next = val

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        return dummy.next
        