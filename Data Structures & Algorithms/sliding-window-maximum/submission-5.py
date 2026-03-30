class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []
        l = r = 0

        while r <len(nums):
            n = nums[r]
            while q and q[-1] < n:
                q.pop()

            q.append(n)

            if r >= k-1:
                output.append(q[0])
                

            if r-l+1 >= k :
                if nums[l] == q[0]:
                    q.popleft()
                l+=1
            r+=1
        return output