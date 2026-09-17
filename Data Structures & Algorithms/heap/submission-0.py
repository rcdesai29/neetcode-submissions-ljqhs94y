class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        # 1. append val
        self.heap.append(val)
        # 2. bubble it upward
        self.bubble_up(len(self.heap)-1)

        pass

    def pop(self) -> int:
        # 1. handle empty
        if not self.heap:
            return -1
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # 2. save root
        root = self.heap[0]
        # 3. move last value to root
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        # 4. bubble it downward

        # 5. return saved root
        return root
        pass

    def top(self) -> int:
        # root is minimum
        if not self.heap:
            return -1
        return self.heap[0]
        

    def heapify(self, nums: list[int]) -> None:
        # do this last
        numsLen = len(nums)
        self.heap = list(nums)
        for i in reversed(range(numsLen //2)):
            self.bubble_down(i)
    
    def bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index -1) // 2
        
    
    def bubble_down(self, index):

        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            # HINT 1:
            if left >= len(self.heap):
                break

            smaller = left

            # HINT 2:
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smaller = right

            # HINT 3:
            if self.heap[smaller] < self.heap[index]:
                self.heap[smaller], self.heap[index] = self.heap[index], self.heap[smaller]     
                index = smaller
            else:
                break