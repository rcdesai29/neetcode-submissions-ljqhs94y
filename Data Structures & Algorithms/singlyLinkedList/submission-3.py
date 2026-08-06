class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.dummy = Node(None)
        self.tail = self.dummy

    
    def get(self, index: int) -> int:
        cur = self.dummy.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1   
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.dummy.next == None:
            self.dummy.next = new_node
            self.tail = new_node
        else:
            old_head = self.dummy.next
            self.dummy.next = new_node
            new_node.next = old_head
           

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        fast = self.dummy.next
        slow = self.dummy
        i = 0
        while i <= index and fast:
            if i == index:
                slow.next = fast.next
                if fast == self.tail:
                    self.tail = slow

                return True
            fast = fast.next
            slow = slow.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        arr = []
        cur = self.dummy.next
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr
        
