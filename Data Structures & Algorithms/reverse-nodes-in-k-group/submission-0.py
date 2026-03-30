# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = dummy

        while True:
            nodeK = self.getKth(start, k)
            if not nodeK:
                break
            nextGroup = nodeK.next

            prev = nodeK.next
            cur = start.next
            while cur != nextGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            tmp = start.next
            start.next = nodeK
            start = tmp
        return dummy.next


    def getKth(self, cur, k):
        while cur and k!=0:
            cur = cur.next
            k-=1
        return cur