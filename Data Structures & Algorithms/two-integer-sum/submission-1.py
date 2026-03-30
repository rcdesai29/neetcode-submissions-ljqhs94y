class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashset = set(nums)
        hashmap = dict() #key: element, def: index

        for i,e in enumerate(nums):
            diff = target - e
            if diff in hashmap:
                return [hashmap[diff], i]
            else: 
                hashmap[e] = i