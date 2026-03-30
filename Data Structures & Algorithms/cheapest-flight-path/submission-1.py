class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = {i: [] for i in range(n)}

        for start, end, cost in flights:
            adj[start].append((end, cost))
        
        q = deque([(src, 0, 0)]) # node, cost, stops
        cheapestCosts = [float('inf')] * n
        best = float('inf')
        while q:

            node, cost, stops = q.popleft()

            if node == dst:
                best = min(best, cost)
                continue
            
            for nei, c in adj[node]:
                if stops < k+1 and cheapestCosts[nei] > cost + c:
                    q.append((nei, cost + c, stops + 1))
                    cheapestCosts[nei] = cost + c
        return best if best != float('inf') else -1

