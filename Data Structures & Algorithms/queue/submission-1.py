class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        

    def append(self, value: int) -> None:
        new_node = ListNode(value)

        previous_node = self.tail.prev
        previous_node.next = new_node
        new_node.prev = previous_node

        new_node.next = self.tail
        self.tail.prev = new_node
        

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)

        next_node = self.head.next
        self.head.next = new_node
        new_node.prev = self.head

        new_node.next = next_node
        next_node.prev = new_node
        

    def pop(self) -> int:
        if self.isEmpty() == True:
            return -1
        

        #PREV_NODE <-> ANS_NODE <-> Tail_Node
        ans_node = self.tail.prev
        prev_node = ans_node.prev

        prev_node.next = ans_node.next
        self.tail.prev = prev_node

        return ans_node.val
        

    def popleft(self) -> int:
        if self.isEmpty() == True:
            return -1
        
        # HEAD <-> ANS <-> NEXT
        ans_node = self.head.next
        next_node = ans_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return ans_node.val
        
