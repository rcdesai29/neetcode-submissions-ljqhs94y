class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        sorted_q = sorted((q,i) for i,q in enumerate(queries))

        idx = 0
        res = [-1] * len(queries)
        minHeap = []
        for q,i in sorted_q:

            while idx < len(intervals) and intervals[idx][0] <= q:
                start, end = intervals[idx]
                dist = end - start + 1
                heapq.heappush(minHeap, [dist, end])
                idx += 1
            
            while minHeap and minHeap[0][-1] < q:
                heapq.heappop(minHeap)
            if minHeap:
                res[i] = minHeap[0][0]
        return res
