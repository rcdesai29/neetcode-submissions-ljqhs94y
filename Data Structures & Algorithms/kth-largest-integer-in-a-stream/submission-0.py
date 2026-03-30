class KthLargest:

    #Constructor
    # takes in a list, WE heapify
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        #make sure the list is only K length
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    
    #Whenever we add we also return the K largest
    #Its a Min Heap, largest are stored first.
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        
