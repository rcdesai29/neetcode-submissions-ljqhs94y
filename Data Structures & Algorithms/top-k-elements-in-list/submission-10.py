class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return k most frequent values
        """
        k most stuff refers to heaps? 
        have heap size of k
        
        """

        buckets = [[] for i in range(len(nums)+1)] 
        counter = Counter(nums)

        for key, value in counter.items():
            buckets[value].append(key)
        print(buckets)
        res = []
        i = len(buckets)-1
        while len(res) < k:
            if buckets[i]:
                res.extend(buckets[i])
            i -=1
        return res
        
