class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.array = [None] * self.cap

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    # size = 1 cap = 1
    def pushback(self, n: int) -> None:
        if self.size >= self.cap:
            self.resize()
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        num = self.array[self.size-1]
        self.size-=1
        return num
        

    def resize(self) -> None:
        new_arr = [None] * (self.cap * 2)
        for i in range(self.cap):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.cap *= 2


    def getSize(self) -> int:
        return self.size 
        
    
    def getCapacity(self) -> int:
        return self.cap
