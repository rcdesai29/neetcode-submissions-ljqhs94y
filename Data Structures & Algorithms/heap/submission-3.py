class MinHeap:
    
    def __init__(self):
        self.heap = [] 
        # 0 based, children are on the right side of it.

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap)-1)

    def pop(self) -> int:
        if  len(self.heap) == 0:
            return -1
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def top(self) -> int:
        if not self.heap:
            return -1
        
        return self.heap[0]
        

    def heapify(self, nums: List[int]) -> None:
        self.heap = list(nums)

        for i in reversed(range((len(self.heap))//2)):
            self._bubble_down(i)

    def _bubble_up(self, index):
        #pushing node(parent) up
        while index >= 0:
            parent = (index - 1) // 2
            if parent >= 0 and self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
    

    
    def _bubble_down(self, index):
        #pushing node(child) down
        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left >= len(self.heap):
                break
            
            smaller = left

            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smaller = right
            if self.heap[smaller] < self.heap[index]:
                self.heap[index], self.heap[smaller] = self.heap[smaller], self.heap[index]
                index = smaller
            else:
                break
        
        