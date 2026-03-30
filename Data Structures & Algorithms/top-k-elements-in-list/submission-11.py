class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        cnt = Counter(nums)

        for key, value in cnt.items():
            buckets[value].append(key)
        
        res = []
        i = len(buckets) - 1
        while len(res) <  k:
            if buckets[i]:
                res.extend(buckets[i])
            i -= 1
        return res
