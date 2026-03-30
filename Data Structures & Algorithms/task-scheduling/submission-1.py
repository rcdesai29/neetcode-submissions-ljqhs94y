class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        time = 0

        q = deque([])

        while heap or q:
            time += 1

            if not heap:
                time = q[0][1]
            else:
                count = abs(heapq.heappop(heap)) -1
                if count:
                    q.append((count, time + n))
            
            if q and q[0][-1] <= time:
                count = q.popleft()[0]
                heapq.heappush(heap, -count)
        return time

