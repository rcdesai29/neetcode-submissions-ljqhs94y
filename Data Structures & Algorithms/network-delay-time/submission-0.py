class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # k is that starting node
        adj = {i : [] for i in range(1, n+1)}

        for ui, vi, ti in times:
            adj[ui].append((vi, ti))
        
        minHeap = [(0, k)] # time, targetNode
        visit = set()
        total = float('-inf')
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            
            visit.add(node)
            total = max(total, time)
            for vi, ti in adj[node]:
                heapq.heappush(minHeap, (ti + time, vi))

        return total if len(visit) == n else -1

