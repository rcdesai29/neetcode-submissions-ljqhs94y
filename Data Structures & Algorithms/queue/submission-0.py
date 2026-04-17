class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# Linked List implmentation of Double Ended Queue
class Deque:
    
    def __init__(self):
        # two dummy nodes and link them
        self.head  = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev  = self.head
        
    def addRight(self, node):
        nxt, prev = self.tail, self.tail.prev
        #connect node to tail
        node.next = nxt

        #connects last previous node to node
        prev.next = node
        node.prev = prev

        #connects tail previous to node
        self.tail.prev = node
    
    def addLeft(self, node):
        prev, nxt = self.head, self.head.next

        # connects head to new node
        prev.next = node
        node.prev = prev

        # connects New node to old first node
        node.next = nxt
        nxt.prev = node

    def removeRight(self):
        previousNode = self.tail.prev
        if previousNode == self.head:
            return -1

        prev, nxt = previousNode.prev, self.tail

        prev.next = nxt
        nxt.prev = prev

        return previousNode.value
    
    def removeLeft(self):
        nextNode = self.head.next
        if nextNode == self.tail:
            return -1
        prev, nxt = self.head, nextNode.next
        
        prev.next = nxt
        nxt.prev = prev
        return nextNode.value


    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = Node(value)
        self.addRight(node)

         

    def appendleft(self, value: int) -> None:
        node = Node(value)
        self.addLeft(node)
        

    def pop(self) -> int:
        return self.removeRight()

    def popleft(self) -> int:
        return self.removeLeft()
