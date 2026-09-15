class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.table = [None] * self.cap
    
    def hash_func(self, key:int) -> int:
        return key % self.cap

    def insert(self, key: int, value: int) -> None:
        index = self.hash_func(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1
        if (self.size / self.cap) >= .5:
            self.resize()



    def get(self, key: int) -> int:
        index = self.hash_func(key)

        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1


    def remove(self, key: int) -> bool:
        index = self.hash_func(key)
        node = self.table[index]

        if not node:
            return False
        else:
            prev = None
            while node:
                if prev and node.key == key:
                    prev.next = node.next
                    self.size -=1
                    return True
                elif node.key == key:
                    self.table[index] = node.next
                    self.size -= 1
                    return True
                prev, node = node, node.next
        return False
        

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        newTable = [None] * (self.cap * 2)
        self.cap = self.cap * 2
        
        for head in self.table:
            cur = head
            while cur:
                next_node = cur.next
                new_index = cur.key % self.cap

                #prepending in new bucket
                cur.next = newTable[new_index]
                newTable[new_index] = cur

                cur = next_node
        self.table = newTable
        
        
        

