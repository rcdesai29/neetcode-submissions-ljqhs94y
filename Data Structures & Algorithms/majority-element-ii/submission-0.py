class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        cap = len(nums) / 3
        counter = Counter(nums)

        for n in counter:
            if counter[n] > cap:
                res.append(n)
        return res
        
            