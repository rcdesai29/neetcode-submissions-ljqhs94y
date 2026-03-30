class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []
        for i in range(len(points)):
            x1, y1 = points[i]
            dist = math.sqrt(((x1-0)**2 + (y1-0)**2))
            heapq.heappush(minHeap, [dist, i])
        
        print(minHeap)
        while len(res) < k:
            dist, point = heapq.heappop(minHeap)
            res.append(points[point])
        return res
        
        