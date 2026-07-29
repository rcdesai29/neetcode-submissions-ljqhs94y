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
            i += 1
            cur = cur.next
        return -1


    def insertHead(self, val: int) -> None:
        node = Node(val)
        #head
        cur = self.dummy.next
        self.dummy.next = node
        node.next = cur
        if self.tail == self.dummy:
            self.tail = node
        

    def insertTail(self, val: int) -> None:
        node = Node(val)
        #tail is on last node
        self.tail.next = node
        self.tail = node
        
        

    def remove(self, index: int) -> bool:
        #head
        cur = self.dummy
        skip = self.dummy.next
        i = 0

        while skip:
            if i == index:
                cur.next = skip.next
                if self.tail == skip:
                    self.tail = cur
                return True
            i += 1
            cur = cur.next
            skip = skip.next
        return False
        

    def getValues(self) -> List[int]:
        cur = self.dummy.next
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr
        
