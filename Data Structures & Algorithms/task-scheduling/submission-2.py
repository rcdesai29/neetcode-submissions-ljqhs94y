class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        count = Counter(tasks)
        heap = [-c for c in count.values()]
        print(heap)
        heapq.heapify(heap)
        time = 0

        q = deque([]) # holds pairs [task, cooldown]

        while heap or q:
            time += 1

            if not heap:
                time = q[0][1]
            else:
                freq = abs(heapq.heappop(heap)) - 1 
                if freq > 0:
                    q.append((freq, time + n))
            
            if q and q[0][1] <= time:
                freq = q.popleft()[0]
                heapq.heappush(heap, -freq)
        return time