class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)
        print(minHeap)
        while len(minHeap) > 1:
            x = abs(heapq.heappop(minHeap))
            y = abs(heapq.heappop(minHeap))
            # X is the largest, Y is the second largest
            if x > y:
                z = x - y
                heapq.heappush(minHeap, -z)
        if len(minHeap) < 1:
            return 0
        return abs(minHeap[0])
