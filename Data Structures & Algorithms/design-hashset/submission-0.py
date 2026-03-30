class MyHashSet:

    def __init__(self):
        self.size = 100
        self.arr = [[] for i in range(self.size)] 


    def add(self, key: int) -> None:
        if not self.contains(key):
            index = key % self.size
            self.arr[index].append(key)
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            index = key % self.size
            self.arr[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.size
        for n in self.arr[index]:
            if key == n:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)