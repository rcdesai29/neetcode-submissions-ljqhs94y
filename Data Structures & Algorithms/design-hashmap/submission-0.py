class MyHashMap:

    def __init__(self):
        self.arr = [[] for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.arr)
        for i in range(len(self.arr[index])):
            pair = self.arr[index][i]
            if pair:
                k, v = pair
                if k == key:
                    self.arr[index][i] = [key, value]
                    return
        self.arr[index].append([key, value])


    def get(self, key: int) -> int:
        index = key % len(self.arr)
        for pair in self.arr[index]:
            if pair:
                k, v = pair
                if k == key:
                    return v
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.arr)
        for pair in self.arr[index]:
            if pair:
                k, v = pair
                if k == key:
                    self.arr[index].remove(pair)
                    return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)