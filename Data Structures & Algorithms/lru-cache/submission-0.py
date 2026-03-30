class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to Node
        self.head, self.tail = Node(0,0), Node(0,0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prevNode = node.prev
        nxtNode = node.next

        prevNode.next = nxtNode
        nxtNode.prev = prevNode

    def insert(self, node):
        prevNode = self.tail.prev
        nxtNode = self.tail

        prevNode.next = node
        nxtNode.prev = node

        node.prev = prevNode
        node.next = nxtNode

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            del self.cache[lru.key]
            self.remove(lru)
        
