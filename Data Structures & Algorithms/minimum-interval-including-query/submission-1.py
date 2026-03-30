class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        res = [-1] * len(queries)

        intervals.sort()

        idx = 0
        minHeap = []
        sortedQ = sorted([[v, i] for i,v in enumerate(queries)])
        for v, i in sortedQ:
            while idx < len(intervals) and intervals[idx][0] <= v:
                start, end = intervals[idx]
                distance = end - start + 1
                heapq.heappush(minHeap, [distance, end])
                idx += 1
            
            while minHeap and minHeap[0][1] < v:
                heapq.heappop(minHeap)
            
            if minHeap:
                res[i] = minHeap[0][0]
        return res
