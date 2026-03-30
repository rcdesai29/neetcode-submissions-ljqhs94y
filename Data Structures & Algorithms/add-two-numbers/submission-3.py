# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we get two nodes that are in reverse
        # a new node is the addition of those two
        # reverse the new node
        cur = dummy = ListNode(0)
        carry = 0
        while l1 and l2:
            newVal = l1.val + l2.val + carry
            if len(str(newVal)) > 1:
                tens = newVal // 10
                ones = newVal % 10
                cur.next = ListNode(ones)
                carry = tens
            else:
                cur.next = ListNode(newVal)
                carry = 0
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        
        while l1:
            newVal = l1.val + carry
            if len(str(newVal)) > 1:
                tens = newVal // 10
                ones = newVal % 10
                cur.next = ListNode(ones)
                carry = tens
            else:
                cur.next = ListNode(newVal)
                carry = 0
            l1 = l1.next
            cur = cur.next
        while l2:
            newVal = l2.val + carry
            if len(str(newVal)) > 1:
                tens = newVal // 10
                ones = newVal % 10
                cur.next = ListNode(ones)
                carry = tens
            else:
                cur.next = ListNode(newVal)
                carry = 0
            l2 = l2.next
            cur = cur.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummy.next
